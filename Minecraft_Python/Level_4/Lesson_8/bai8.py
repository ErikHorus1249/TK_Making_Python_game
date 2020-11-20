
import mcpi.minecraft as minecraft
import mcpi.block as block
from minecraftstuff import *
import math
import random
import time

# khoang cach giua hai diem 

def distanceBetweenPoints(p1, p2):
    xd = p1.x - p2.x
    yd = p1.y - p2.y
    zd = p1.z - p2.z

    return math.sqrt(pow(xd)+pow(yd)+pow(zd))


HOVER_HEIGHT =  15
ALIEN_SP = ["<ALIENT>U can't run forever",
            "<ALIENT>Resistance is useless",
            "<ALIENT>We only wanna be friend"]


mc = minecraft.Minecraft.create()
mcdrawing = MinecraftDrawing(mc)

alienPos = mc.player.getTilePos()
alienPos.y += 50

mode = "landing"

alienBlock = [minecraftstuff.ShapeBlock(-1,0,0,17,5),
              minecraftstuff.ShapeBlock(0,0,-1,17,5),
              minecraftstuff.ShapeBlock(1,0,0,17,5),
              minecraftstuff.ShapeBlock(0,0,1,17,5),
              minecraftstuff.ShapeBlock(0,-1,0,1,5),
              minecraftstuff.ShapeBlock(0,1,0,1,5)]

alienShape = MinecraftShape(mc, alienPos, alienBlock)

while mode != "missioncompleted":

    # get player position
    playerPos = mc.player.getTilePos()

    if mode == "landing":
        mc.postToChat("<ALIENTS>We dont come in peace - please panic")
        alienTarget = playerPos.clone()
        alienTarget.y = alienTarget.y + HOVER_HEIGHT
        mode = "attack"
    elif mode == "attack":
        # kiem tra neu alien o tren dau nguoi choi
        if alienPos.x == playerPos.x and alienPos.z == playerPos.z:
            mc.postToChat("<ALIEN>We have U now")

            # tao phong
            mc.setBlocks(0,50,0,6,56,6,133)
            mc.setBlocks(1,51,1,5,55,5,0)
            mc.setBlock(3,5,3,49)

            # giam nguoi choi

            mc.player.setTilePos(3,51,5)
            time.sleep(10)
            mc.postToChat("<ALIEN>Not very interesting at all - send it back")
            time.sleep(2)
            
            # tha ve cho cu 
            mc.player.setTilePos(playerPos.x, playerPos.y, playerPos.z)

            # xoa phong giam 
            mc.setBlocks(0,50,0,6,56,6,0)

            mode = "missioncompleted"
        else:
            # player chay thoat 
            mc.postToChat(ALIEN_SP[random.randint(0, len(ALIEN_SP)-1)])
            alienPos = playerPos.clone()
            alienTarget.y += HOVER_HEIGHT
        
    if alienPos != alienTarget:
 # thay doi vi tri cua alien 
        blockBtw = mcdrawing.getLine(alienPos.x, alienPos.y, alienPos.z, alienTarget.x, alienTarget.y, alienTarget.z)
# vong lap lay toa do theo doi ngouoi choi
        for blockBetween in blockBtw:
            
            alienShape.move(blockBetween.x, blockBetween.y, blockBetween.z)

            time.sleep(0.25)


        alienPos = alienTarget.clone()

alienShape.clear()       
