import asyncio
from telethon import TelegramClient
from telethon.tl.types import Channel

api_id =                  # <-- put your api_id (INT)
api_hash = ""   # <-- put your api_hash (STRING)
session_name = "telegram_session"

BLOCK_MESSAGES = {
    "This channel is unavailable due to copyright infringement.",
    "This channel can’t be displayed because it violated Telegram's Terms of Service."
}

async def main():
    client = TelegramClient(session_name, api_id, api_hash)
    await client.start()

    print("\n🔍 Scanning for blocked channels...\n")

    blocked_channels = {}

    async for dialog in client.iter_dialogs():
        if not isinstance(dialog.entity, Channel):
            continue

        channel = dialog.entity
        name = dialog.name or "Unknown"

        if getattr(channel, "restricted", False):
            for r in channel.restriction_reason:
                if r.text in BLOCK_MESSAGES:
                    if channel.id not in blocked_channels:
                        blocked_channels[channel.id] = name
                        print(f"❌ {name}  |  ID: {channel.id}")
                    break

    if not blocked_channels:
        print("\n✅ No blocked channels found.")
        await client.disconnect()
        return

    print("\n==============================")
    print(f"📄 Total blocked channels: {len(blocked_channels)}")
    print("==============================")

    choice = input("\nLeave all channels? (type yes): ").strip().lower()

    if choice == "yes":
        print("\n🚪 Leaving channels...\n")
        for ch_id, name in blocked_channels.items():
            try:
                await client.delete_dialog(ch_id)
                print(f"✔ Left: {name} (ID: {ch_id})")
            except Exception as e:
                print(f"⚠️ Failed to leave {name}: {e}")
    else:
        print("\n❎ No channels were left.")

    await client.disconnect()

asyncio.run(main())
