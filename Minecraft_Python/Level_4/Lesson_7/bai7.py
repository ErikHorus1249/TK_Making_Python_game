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

mc = Minecraft.create()

mcdrawing = MinecraftDrawing(mc)

pos = mc.player.getTilePos()

clockMiddle = pos
clockMiddle.y = clockMiddle.y + 25

CLOCK_RADIUS = 20

HOUR_HAND_LENG = 10
MIN_HAND_LENG = 18
SEC_HAND_LENG = 20

mcdrawing.drawCircle(clockMiddle.x, clockMiddle.y, clockMiddle.z,
			CLOCK_RADIUS, 57)

while True:
	timeNow = datetime.datetime.now()
	#hour
	hours = timeNow.hour 
	
	if hours >= 12:
		hours = timeNow.hour - 12
	
	minutes = timeNow.minute
	
	seconds = timeNow.second
	
	
	hourHandAngle = (360/12) * hours
	
	hourHandX, hourHandY = findPointOnCircle(clockMiddle.x, clockMiddle.y, HOUR_HAND_LENG, hourHandAngle)
# HOUR
	mcdrawing.drawLine(clockMiddle.x, clockMiddle.y, clockMiddle.z,
	hourHandX, hourHandY, clockMiddle.z, block.DIRT.id)


	minHandAngle = (360/60) * minutes

	minHandX, minHandY = findPointOnCircle(clockMiddle.x, clockMiddle.y, MIN_HAND_LENG, minHandAngle)
# MIN
	mcdrawing.drawLine(clockMiddle.x, clockMiddle.y, clockMiddle.z-1, minHandX, minHandY, clockMiddle.z-1,block.WOOD_PLANKS.id)



	secHandAngle = (360/60) * seconds

	secHandX, secHandY = findPointOnCircle(clockMiddle.x, clockMiddle.y, SEC_HAND_LENG, secHandAngle)
# SEC
	mcdrawing.drawLine(clockMiddle.x, clockMiddle.y, clockMiddle.z+1, secHandX, secHandY, clockMiddle.z+1, block.STONE.id)

	time.sleep(0.01)
# Xoa 
	mcdrawing.drawLine(clockMiddle.x, clockMiddle.y, clockMiddle.z, hourHandX, hourHandY, clockMiddle.z, 0)

	mcdrawing.drawLine(clockMiddle.x, clockMiddle.y, clockMiddle.z-1, minHandX, minHandY, clockMiddle.z-1,0)

	mcdrawing.drawLine(clockMiddle.x, clockMiddle.y, clockMiddle.z+1, secHandX, secHandY, clockMiddle.z+1, 0)


		
		
		
		
		





