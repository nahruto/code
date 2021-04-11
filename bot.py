
# import ~
import discord, datetime, asyncio, random, time


# 봇 설정
token = "ODE1ODUwMDg3MDQ5MTk5NjI2.YDyZmg.BLLwt5oPVuwsYW_yTpU9SeXaqDs"
code = discord.Client()
ehs = 100

# 봇 실행
@code.event
async def on_ready():
    await code.change_presence(activity=discord.Game(name='코드는 코드친서버의 AI야!'))
    print('실행 중......')
    time.sleep(3 or 4 or 5 or 6)
    print('실행 성공!')
    time.sleep(1)
    input("앤터키를 눌러줘! > ")
    time.sleep(1)
    print('안녕? 나는 디스코드 봇 코드야.')
    time.sleep(1)
    print(f'{code.user}에 로그인했어!')


# 봇 명령어
@code.event
async def on_message(message):

    # 변수
    user = message.author

    # 인사
    if message.content == "코드야 안녕":
        await message.channel.send(f'{message.author.mention}, 안녕?')

    # 대답
    if message.content == "코드야":
        await message.channel.send('응?')

    # 명령어
    if message.content == "코드야 명령어":
        embed = discord.Embed(colour=discord.Colour.red(), title="코드의 명령어!", description="이거슨 코드의 명령어야!")
        embed.add_field(name="코드야", value="응?", inline=False)
        embed.add_field(name="코드야 안녕", value="(닉네임), 안녕?", inline=False)
        embed.add_field(name="코드야 내정보", value="(닉네임)의 정보", inline=False)
        embed.add_field(name="코드야 10초(30초, 1분, 5분, 10분)타이머", value="10초(30초, 1분, 5분, 10분)타이머", inline=False)
        embed.add_field(name="코드야 청소", value="청소할 채팅 갯수를 관리자에게 알려줘", inline=False)
        embed.add_field(name="코드야 가위바위보", value="가위.....바위......보!", inline=False)
        await message.channel.send(embed=embed)

    # 정보
    if message.content == '코드야 내정보':
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        await message.channel.send(f'이름은 {user.name}, 아이디는 {user.id}, 닉네임은 {user.display_name}')
        await message.channel.send(f'가입일은 {date.year}년 {date.month}월 {date.day}일')
    if message.content == '코드야 프로필':
        await message.channel.send(f'프로필 사진은 {user.avatar_url}')

    # 10초 타이머
    if message.content == "코드야 10초타이머":
        await asyncio.sleep(10)
        await message.channel.send('10초가 끝났어!')

    # 30초 타이머
    if message.content == "코드야 30초타이머":
        await asyncio.sleep(30)
        await message.channel.send('30초가 끝났어!')

    # 1분 타이머
    if message.content == "코드야 1분타이머":
        await asyncio.sleep(60)
        await message.channel.send('1분이 끝났어!')

    # 5분 타이머
    if message.content == "코드야 5분타이머":
        await asyncio.sleep(300)
        await message.channel.send('5분이 끝났어!')

    # 10분 타이머
    if message.content == "코드야 10분타이머":
        await asyncio.sleep(600)
        await message.channel.send('10분이 끝났어!')

    # 채팅 청소
    if message.content.startswith("코드야 청소"):
        number = int(input("청소할수 > "))
        await message.delete()
        await message.channel.purge(limit=number)
        await message.channel.send(f'{number}개의 채팅을 청소했어!')

    # 상태메세지
    if message.content.startswith("코드야 상태메세지"):
        tkdxo = str(input("할일 > "))
        await code.change_presence(activity=discord.Game(name=f'{tkdxo}'))

    # 가위바위보
    if message.content.startswith("코드야 가위바위보"):
        msg = await message.channel.send('가위.....')
        await msg.add_reaction("\U0000270C")
        await asyncio.sleep(1)
        await msg.edit(content='바위.....')
        await msg.add_reaction("\U0000270A")
        await asyncio.sleep(1)
        await msg.edit(content='보!')
        await msg.add_reaction("\U0000270B")

    # 랜덤
    if message.content.startswith("코드야 랜덤"):
        await message.add_reaction("\U00000032\U0000FE0F\U000020E3")
        await message.add_reaction("\U00000033\U0000FE0F\U000020E3")
        await message.add_reaction("\U00000034\U0000FE0F\U000020E3")
        await message.add_reaction("\U00000035\U0000FE0F\U000020E3")
        await message.add_reaction("\U00000036\U0000FE0F\U000020E3")


# 이모지
@code.event
async def on_reaction_add(reaction, user):

    if user.bot == 1:
        return None

    # '가위'인지 '바위'인지 '보'인지 정하는 변수
    num = random.randint(1, 3)

    # 가위바위보
    # 가위
    if str(reaction.emoji) == "\U0000270C":
        ehs-5
        if num == 1:
            await reaction.message.channel.send(user.name + " > 가위")
            await reaction.message.channel.send("코드 > 가위")
            await asyncio.sleep(0.5)
            await reaction.message.channel.send("비겼어")
            ehs+5
        if num == 2:
            await reaction.message.channel.send(user.name + " > 가위")
            await reaction.message.channel.send("코드 > 바위")
            await asyncio.sleep(0.5)
            await reaction.message.channel.send(user.name + "이(가) 졌어")
            
        if num == 3:
            await reaction.message.channel.send(user.name + " > 가위")
            await reaction.message.channel.send("코드 > 보")
            await asyncio.sleep(0.5)
            await reaction.message.channel.send(user.name + "이(가) 이겼어")
            ehs+10
    # 바위
    if str(reaction.emoji) == "\U0000270A":
        ehs-5
        if num == 1:
            await reaction.message.channel.send(user.name + " > 바위")
            await reaction.message.channel.send("코드 > 가위")
            await asyncio.sleep(0.5)
            await reaction.message.channel.send(user.name + "이(가) 이겼어")
            ehs+10
        if num == 2:
            await reaction.message.channel.send(user.name + " > 바위")
            await reaction.message.channel.send("코드 > 바위")
            await asyncio.sleep(0.5)
            await reaction.message.channel.send("비겼어")
            ehs+5
        if num == 3:
            await reaction.message.channel.send(user.name + " > 바위")
            await reaction.message.channel.send("코드 > 보")
            await asyncio.sleep(0.5)
            await reaction.message.channel.send(user.name + "이(가) 졌어")
            
    # 보
    if str(reaction.emoji) == "\U0000270B":
        ehs-5
        if num == 1:
            await reaction.message.channel.send(user.name + " > 보")
            await reaction.message.channel.send("코드 > 가위")
            await asyncio.sleep(0.5)
            await reaction.message.channel.send(user.name + "이(가) 졌어")
            
        if num == 2:
            await reaction.message.channel.send(user.name + " > 보")
            await reaction.message.channel.send("코드 > 바위")
            await asyncio.sleep(0.5)
            await reaction.message.channel.send(user.name + "이(가) 이겼어")
            ehs+10
        if num == 3:
            await reaction.message.channel.send(user.name + " > 보")
            await reaction.message.channel.send("코드 > 보")
            await asyncio.sleep(0.5)
            await reaction.message.channel.send("비겼어")
            ehs+5
    # 랜덤
    if str(reaction.emoji) == "\U00000032\U0000FE0F\U000020E3":
        num = random.randint(1, 2)
        await reaction.message.channel.send(num)
    if str(reaction.emoji) == "\U00000033\U0000FE0F\U000020E3":
        num = random.randint(1, 3)
        await reaction.message.channel.send(num)
    if str(reaction.emoji) == "\U00000034\U0000FE0F\U000020E3":
        num = random.randint(1, 4)
        await reaction.message.channel.send(num)
    if str(reaction.emoji) == "\U00000035\U0000FE0F\U000020E3":
        num = random.randint(1, 5)
        await reaction.message.channel.send(num)
    if str(reaction.emoji) == "\U00000036\U0000FE0F\U000020E3":
        num = random.randint(1, 6)
        await reaction.message.channel.send(num)
    
        
# 봇 루프
code.run(token)