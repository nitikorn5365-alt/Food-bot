import discord
from discord import app_commands
import random
import os

TOKEN = os.environ["TOKEN"]

foods = [
    "ข้าวกะเพราไก่","ข้าวกะเพราหมู","ข้าวกะเพราหมูกรอบ","ข้าวกะเพราเนื้อ","ข้าวกะเพราทะเล",
    "ข้าวผัดหมู","ข้าวผัดไก่","ข้าวผัดกุ้ง","ข้าวผัดปู","ข้าวผัดทะเล",
    "ข้าวมันไก่","ข้าวหมูแดง","ข้าวหมูกรอบ","ข้าวหน้าเป็ด","ข้าวขาหมู","ข้าวคลุกกะปิ",
    "ข้าวไข่เจียว","ข้าวไข่เจียวหมูสับ","ข้าวไข่ข้น","ข้าวหมูกระเทียม","ข้าวไก่กระเทียม",
    "ข้าวผัดพริกแกง","ข้าวผัดพริกเกลือ","ข้าวผัดต้มยำ",
    "ผัดไทย","ผัดซีอิ๊ว","ราดหน้า",
    "ก๋วยเตี๋ยวเรือ","ก๋วยเตี๋ยวต้มยำ","ก๋วยเตี๋ยวหมูน้ำใส","ก๋วยเตี๋ยวเนื้อ","ก๋วยเตี๋ยวเย็นตาโฟ",
    "บะหมี่หมูแดง","บะหมี่เกี๊ยว","บะหมี่เกี๊ยวหมูแดง",
    "ส้มตำ","ส้มตำไทย","ส้มตำปูปลาร้า","ส้มตำไข่เค็ม","ส้มตำทะเล",
    "ลาบหมู","ลาบไก่","ลาบเนื้อ","น้ำตกหมู","น้ำตกเนื้อ",
    "ต้มยำกุ้ง","ต้มยำทะเล","ต้มข่าไก่",
    "แกงเขียวหวานไก่","แกงเขียวหวานหมู","แกงแดง","แกงพะแนง","แกงมัสมั่น","แกงส้ม","แกงป่า",
    "แกงจืดเต้าหู้หมูสับ","แกงจืดวุ้นเส้น","ต้มจืดตำลึง","ไข่พะโล้",
    "หมูทอดกระเทียม","ไก่ทอด","หมูแดดเดียว","คอหมูย่าง","หมูกระทะ","ไก่ย่าง",
    "ปลานึ่งมะนาว","ปลาทอดน้ำปลา","ปลากะพงทอด",
    "ยำวุ้นเส้น","ยำมาม่า","ยำทะเล","ยำหมูยอ","ยำไข่ดาว"
]

OWNER_ID = int(os.environ.get("OWNER_ID", "0"))  # ใส่ใน Render env ได้

class Bot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        # ❌ ไม่ sync อัตโนมัติ กันโดน 429
        pass

client = Bot()

@client.event
async def on_ready():
    print(f"Bot Online: {client.user}")

@client.tree.command(name="กินไรดี", description="สุ่มเมนูอาหาร")
async def food(interaction: discord.Interaction):
    await interaction.response.send_message(f"วันนี้กิน **{random.choice(foods)}** ดีไหม 🍜")

@client.tree.command(name="sync", description="Sync commands (owner only)")
async def sync(interaction: discord.Interaction):
    if OWNER_ID and interaction.user.id != OWNER_ID:
        return await interaction.response.send_message("เฉพาะเจ้าของบอทเท่านั้น", ephemeral=True)

    await client.tree.sync()
    await interaction.response.send_message("Synced ✅", ephemeral=True)

client.run(TOKEN)