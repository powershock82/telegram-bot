import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from google import genai

# Configura le chiavi leggendole dall'ambiente
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# Inizializza il client di Gemini
client = genai.Client(api_key=GEMINI_API_KEY)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    
    # Istruzione per dare il tono desiderato al bot
    system_instruction = (
        "Sei un assistente virtuale spiritoso, amichevole e pronto alla battuta. "
        "Rispondi sempre in modo naturale, divertente e colloquiale."
    )
    
    try:
        # Richiesta a Gemini usando il modello standard
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_message,
            config={
                'system_instruction': system_instruction,
            }
        )
        reply_text = response.text
    except Exception as e:
        reply_text = "Ops, ho avuto un piccolo blackout mentale! Riprova tra un attimo."

    await update.message.reply_text(reply_text)

if name == 'main':
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    
    # Ascolta tutti i messaggi di testo
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    
    print("Bot avviato con successo!")
    app.run_polling()