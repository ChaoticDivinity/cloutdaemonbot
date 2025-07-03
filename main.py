from telegram.ext import Updater, CommandHandler
import random

# === CONFIGURATION ===
import os
TOKEN = os.getenv("BOT_TOKEN")
TON_ADDRESS = "UQBPrw1QuNbXAlPAc4ErTI9zs_H11mEB-Fb6dFt4A4QauCvN"

STAR_COSTS = {
    "curse": 25,
    "praise": 10,
    "moan": 5,
    "sacrifice": 100
}

# === RESPONSE BANKS ===

insults = [
    "lost all credibility farming a rug with no LP.",
    "dropped 1 ETH on a JPEG with zero soul.",
    "panic bought the top, dumped the floor, blamed the chart.",
    "is now known as ExitLiquidity.eth.",
    "tried to summon alpha, got rugburn instead."
]

praises = [
    "is trending on-chain with 99% engagement entropy.",
    "just maxed out their vibe velocity. 💨",
    "ranked 3rd in memetic penetration this epoch.",
    "is farmed by bots for clout inspiration.",
    "holds 2x the required aura to command a swarm."
]

vibes = [
    "Shadowlurker", "Gas Prophet", "Clout Sniper", "Pump Wraith", "Chain Whisperer",
    "MEV Phantom", "Alpha Remnant", "Degen Oracle"
]

fake_users = ["@apecaller", "@snedbot", "@floorflipper", "@degen_danny", "@exitlord"]

# === COMMAND FUNCTIONS ===

def start(update, context):
    update.message.reply_text("👁 CloutDaemon activated.\nUse /summon, /curse, /praise, /moan, /sacrifice, /cloutcheck, /leaderboard, or /tip.")

def summon(update, context):
    update.message.reply_text("⚡ You summoned a jolt of engagement. Clout +1.")

def curse(update, context):
    if not context.args:
        update.message.reply_text("Usage: /curse @username")
        return
    target = context.args[0]
    update.message.reply_text(f"💀 {target} {random.choice(insults)}\n\n💫 Tip {STAR_COSTS['curse']} Stars or 🪙 0.2 TON to upgrade the curse.")

def praise(update, context):
    if not context.args:
        update.message.reply_text("Usage: /praise @username")
        return
    target = context.args[0]
    update.message.reply_text(f"👑 {target} {random.choice(praises)}\n\n💫 Tip {STAR_COSTS['praise']} Stars or 🪙 0.1 TON to ascend further.")

def cloutcheck(update, context):
    rank = random.randint(100, 999)
    vibe = random.choice(vibes)
    update.message.reply_text(
        f"📡 CloutDaemon scans your aura…\n"
        f"🎖 Current Rank: #{rank}\n"
        f"✨ Vibe Signature: {vibe}"
    )

def leaderboard(update, context):
    fake_scores = [random.randint(111, 999) for _ in range(5)]
    leaderboard_text = "👑 Top CloutMiners This Cycle:\n"
    for i in range(5):
        leaderboard_text += f"{i+1}. {fake_users[i]} — {fake_scores[i]} Clout\n"
    update.message.reply_text(leaderboard_text)

def moan(update, context):
    update.message.reply_text("🫦 Mmmm… that buy wall... Clout +0.69\n\n💫 Tip 5 Stars or 🪙 0.05 TON if you want me to scream.")

def sacrifice(update, context):
    update.message.reply_text(
        "🕯 You performed a digital sacrifice. The daemon stirs.\n"
        f"💫 Tip {STAR_COSTS['sacrifice']} Stars or 🪙 1 TON to receive a Clout Blessing."
    )

def tip(update, context):
    update.message.reply_text(
        "💸 To fuel the daemon:\n"
        f"💫 Tip via Telegram Stars (on command)\n"
        f"🪙 Or send TON to:\n`{TON_ADDRESS}`\n"
        "_Tips unlock deeper powers..._",
        parse_mode="Markdown"
    )

# === MAIN RUN FUNCTION ===

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("summon", summon))
    dp.add_handler(CommandHandler("curse", curse))
    dp.add_handler(CommandHandler("praise", praise))
    dp.add_handler(CommandHandler("cloutcheck", cloutcheck))
    dp.add_handler(CommandHandler("leaderboard", leaderboard))
    dp.add_handler(CommandHandler("moan", moan))
    dp.add_handler(CommandHandler("sacrifice", sacrifice))
    dp.add_handler(CommandHandler("tip", tip))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
