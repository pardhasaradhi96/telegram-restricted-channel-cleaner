import asyncio
from telethon import TelegramClient
from telethon.tl.types import Channel

# 🔹 YOUR API DETAILS
api_id =         # your api_id
api_hash = ""  # your api_hash
session_name = "telegram_session"

TARGET_MESSAGE = "This channel is unavailable due to copyright infringement."

async def main():
    client = TelegramClient(session_name, api_id, api_hash)
    await client.start()

    print("\n🔍 Scanning for copyright-blocked channels...\n")

    blocked_channels = []  # list of (id, access_hash, name)

    async for dialog in client.iter_dialogs():
        if not isinstance(dialog.entity, Channel):
            continue

        channel = dialog.entity
        name = dialog.name

        if getattr(channel, "restricted", False):
            for r in channel.restriction_reason:
                if r.reason == "copyright" and r.text == TARGET_MESSAGE:
                    print(f"❌ {name}  |  ID: {channel.id}")
                    blocked_channels.append(
                        (channel.id, channel.access_hash, name)
                    )
                    break

    if not blocked_channels:
        print("\n✅ No copyright-blocked channels found.")
        await client.disconnect()
        return

    print("\n==============================")
    print(f"📄 Total blocked channels: {len(blocked_channels)}")
    print("==============================")

    choice = input("\nLeave all channels? (type yes): ").strip().lower()

    if choice == "yes":
        print("\n🚪 Leaving channels...\n")
        for ch_id, access_hash, name in blocked_channels:
            try:
                await client.delete_dialog(ch_id)
                print(f"✔ Left: {name} (ID: {ch_id})")
            except Exception as e:
                print(f"⚠️ Failed to leave {name}: {e}")
    else:
        print("\n❎ No channels were left.")

    await client.disconnect()

asyncio.run(main())
