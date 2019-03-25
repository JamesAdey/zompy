from gameobject import *

class ItemManager(GameObject):

    '''
        This system could
    '''

    # all our items are circles
    items = []
    
    def add_item(self,item):
        if(item not in self.items):
            self.items.append(item)

    def remove_item(self,item):
        if(item in self.items):
            self.items.remove(item)

    def update(self,gameGlobals):

        for player in gameGlobals.players:
            
            for item in self.items:
            
                # check circle overlap with the player
                dx = item.x - player.x
                dy = item.y - player.y
    
                # compute the combined radius
                radius = item.get_collision_radius() + player.get_collision_radius()
    
                # square the values and compare square distances
                sqrRadius = radius * radius
                sqrDist = (dx*dx)+(dy*dy)
    
                if(sqrDist < sqrRadius):
                    # notify both participants of collision
                    item.on_collision(gameGlobals, player)
                    player.on_collision(gameGlobals, item)
                
