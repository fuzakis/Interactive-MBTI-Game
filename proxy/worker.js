/**
 * MBTI Game — Proxy API OpenAI (Cloudflare Worker)
 *
 * Tugas worker ini satu: menerima request dari game Ren'Py TANPA API key,
 * menempelkan API key (tersimpan sebagai encrypted secret di Cloudflare),
 * lalu meneruskannya ke OpenAI dan mengembalikan jawabannya apa adanya.
 *
 * Secrets/variables yang dipakai (diatur di dashboard Cloudflare,
 * menu Settings > Variables and Secrets pada worker ini):
 *   - OPENAI_API_KEY  (wajib, tipe Secret)  : API key OpenAI kamu
 *   - APP_TOKEN       (opsional, tipe Secret): token sederhana untuk menyaring
 *       request iseng. Kalau di-set, game harus mengirim header X-App-Token
 *       dengan nilai yang sama (isi PROXY_APP_TOKEN di game/.env).
 *
 * Proteksi bawaan:
 *   - Hanya menerima POST dengan body JSON.
 *   - Model dibatasi whitelist (gpt-4o & fine-tune turunannya).
 *   - max_tokens dipagari maksimal 2000 (limit terbesar yang dipakai game).
 *   - Tidak menyimpan/melog isi percakapan.
 */

const OPENAI_URL = "https://api.openai.com/v1/chat/completions";
const MAX_TOKENS_CAP = 2000;

function isAllowedModel(model) {
  return model === "gpt-4o" || model.startsWith("ft:gpt-4o");
}

export default {
  async fetch(request, env) {
    if (request.method !== "POST") {
      return new Response(JSON.stringify({ error: "Method not allowed" }), {
        status: 405,
        headers: { "Content-Type": "application/json" },
      });
    }

    // Saringan opsional: token aplikasi
    if (env.APP_TOKEN) {
      const token = request.headers.get("X-App-Token");
      if (token !== env.APP_TOKEN) {
        return new Response(JSON.stringify({ error: "Unauthorized" }), {
          status: 401,
          headers: { "Content-Type": "application/json" },
        });
      }
    }

    let body;
    try {
      body = await request.json();
    } catch (e) {
      return new Response(JSON.stringify({ error: "Invalid JSON body" }), {
        status: 400,
        headers: { "Content-Type": "application/json" },
      });
    }

    // Validasi bentuk request agar endpoint tidak disalahgunakan
    const model = String(body.model || "");
    if (!isAllowedModel(model) || !Array.isArray(body.messages)) {
      return new Response(JSON.stringify({ error: "Request not allowed" }), {
        status: 400,
        headers: { "Content-Type": "application/json" },
      });
    }
    if (!Number.isFinite(body.max_tokens) || body.max_tokens > MAX_TOKENS_CAP) {
      body.max_tokens = MAX_TOKENS_CAP;
    }

    // Teruskan ke OpenAI dengan key dari secret
    const resp = await fetch(OPENAI_URL, {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${env.OPENAI_API_KEY}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });

    // Kembalikan respons OpenAI apa adanya (status + body JSON),
    // sehingga sisi game tidak perlu diubah format parsing-nya.
    return new Response(resp.body, {
      status: resp.status,
      headers: { "Content-Type": "application/json" },
    });
  },
};
