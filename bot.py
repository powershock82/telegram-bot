import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from openai import openai

# Configura le chiavi leggendole dall'ambiente
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Inizializza il client di OPENAI
client = Openai (api_key=OPENAI_API_KEY)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    
    # Istruzione per dare il tono desiderato al bot
    system_instruction = (
        "Sei un uomo spiritoso, amichevole,a volgare, ubriacone e pronto alla battuta. "
        "Rispondi sempre in modo naturale, divertente e colloquiale."
    )
    
    try:
        # Richiesta a openai usando il modello standard
        response = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role": "system", "content": 
        system_instruction}, {"role": "user", "content": user_message}]) 
           
                
           
      
        reply_text = response.choices[0].message.content
    except Exception as e:
        reply_text = "Ops, sono ubriaco e mi si sono incrociate le spade! Riprova tra un attimo."

    await update.message.reply_text(reply_text)

if __name__== '__main__':
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    
    # Ascolta tutti i messaggi di testo
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    
    print("Bot avviato con successo!")
    app.run_polling()
