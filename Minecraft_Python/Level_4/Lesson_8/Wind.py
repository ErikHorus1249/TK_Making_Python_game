

from minecraftstuff import MinecraftDrawing
from mcpi.minecraft import Minecraft
from mcpi import block
import time
import datetime
import math

def findPointOnCircle(cx, cy, radius, angle):
	x = cx + math.sin(math.radians(angle))* radius
	y = cy + math.cos(math.radians(angle)) * radius
	x = int(round(x, 0))
	y = int(round(y, 0))
	return(x,y)

def drawCenter(x,y,z):
	mcdrawing.drawSphere(x,y,z,4,49)
	
def drawPipe(x,y,z):
	i = y
	while(i>0):
		mcdrawing.drawHollowSphere(x,i,z,3,42)
		i -= 1
	
mc = Minecraft.create()

mcdrawing = MinecraftDrawing(mc)

pos = mc.player.getTilePos()

clockMiddle = pos
clockMiddle.y = clockMiddle.y + 25



SEC_HAND_LENG = 60

#mcdrawing.drawCircle(clockMiddle.x, clockMiddle.y, clockMiddle.z,CLOCK_RADIUS, 57)

drawCenter(clockMiddle.x,clockMiddle.y,clockMiddle.z)
drawPipe(clockMiddle.x,clockMiddle.y,clockMiddle.z-2)
while True:
	
	timeNow = datetime.datetime.now()

	seconds = timeNow.second

	secHandAngle1 = (360/60) * seconds
	secHandAngle2 = (360/60) * (seconds + 20)
	secHandAngle3 = (360/60) * (seconds + 40)

	secHandX1, secHandY1 = findPointOnCircle(clockMiddle.x, clockMiddle.y, SEC_HAND_LENG, secHandAngle1)
	secHandX2, secHandY2 = findPointOnCircle(clockMiddle.x, clockMiddle.y, SEC_HAND_LENG, secHandAngle2)
	secHandX3, secHandY3 = findPointOnCircle(clockMiddle.x, clockMiddle.y, SEC_HAND_LENG, secHandAngle3)
# SEC
	mcdrawing.drawLine(clockMiddle.x, clockMiddle.y, clockMiddle.z+1, secHandX1, secHandY1, clockMiddle.z+1, block.STONE.id)
	mcdrawing.drawLine(clockMiddle.x, clockMiddle.y, clockMiddle.z+1, secHandX2, secHandY2, clockMiddle.z+1, block.STONE.id)
	mcdrawing.drawLine(clockMiddle.x, clockMiddle.y, clockMiddle.z+1, secHandX3, secHandY3, clockMiddle.z+1, block.STONE.id)
	
	time.sleep(1)
	
# Xoa 

	mcdrawing.drawLine(clockMiddle.x, clockMiddle.y, clockMiddle.z+1, secHandX1, secHandY1, clockMiddle.z+1, 0)
	mcdrawing.drawLine(clockMiddle.x, clockMiddle.y, clockMiddle.z+1, secHandX2, secHandY2, clockMiddle.z+1, 0)
	mcdrawing.drawLine(clockMiddle.x, clockMiddle.y, clockMiddle.z+1, secHandX3, secHandY3, clockMiddle.z+1, 0)


		
		
		
		
		





