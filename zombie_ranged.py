from zombie import *

class RangedZombie(Zombie):

    # range in pixels
    attackRange = 20
    # delay in seconds
    attackDelay = 0.3
    # when we can attack next
    nextAttackTime = 0

    def update(self, gameGlobals):

        currentCell = gameGlobals.navGrid.closest_cell_to(self)
        goal = currentCell.goal

        if(goal == None):
            (targetX,targetY) = currentCell.center
        else:
            (targetX,targetY) = goal.center

        # move towards the player
        self.move(targetX,targetY)

        self.attack(gameGlobals,gameGlobals.player)

        if(self.health <= 0):
            self.dead(gameGlobals)

    def move(self,targetX,targetY):
        moveX = 0
        moveY = 0
        
        if(targetX < self.x):
            moveX = -self.speed
        elif(targetX > self.x):
            moveX = self.speed

        if(targetY < self.y):
            moveY = -self.speed
        elif(targetY > self.y):
            moveY = self.speed
        
        self.x = self.x + moveX
        self.y = self.y + moveY


    def attack(self,gameGlobals,target):

        # check range to target
        (targetX,targetY) = target.get_position()
        dx = targetX - self.x
        dy = targetY - self.y
        sqrDist = (dx*dx)+(dy*dy)

        # our attack is just a big circle collision check
        # imagine we have a larger collision circle than we do
        # then just try that
        realRange = self.radius + target.get_collision_radius()
        realRange += self.attackRange
        
        sqrRange = realRange*realRange

        isInRange = sqrDist < sqrRange
        canAttack = self.nextAttackTime < gameGlobals.realTime

        if(isInRange and canAttack):
            self.nextAttackTime = gameGlobals.realTime + self.attackDelay
            gameGlobals.bulletManager.fire_bullet(self.x,self.y,targetX,targetY)
            target.take_damage(self.damage)

    
