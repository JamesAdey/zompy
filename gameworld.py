
class GameWorld(object):

    # all our obstacles are circles for now
    obstacles = []

    def add_obstacle(self,obs):
        if(obs not in self.obstacles):
            self.obstacles.append(obs)

    def remove_obstacle(self,obs):
        if(obs in self.obstacles):
            self.obstacles.remove(obs)
    
    def traceline(self,startX,startY,endX,endY):

        '''
        Here anonymous tuples of (x,y) have been used for vector
        arithmetic and ease of understanding.
        It is annoying that Python lacks sensible value-type structure support.
        '''
        
        # compute the constants
        a = (startX,startY)
        b = (endX,endY)
        ab = (endX-startX,endY-startY)
        ab_sqrMag = self.sqrMag(ab)

        # avoid divide by 0
        if(ab_sqrMag == 0):
            return None

        # variables to store the resulting value
        closest = None
        frc = 1.0

        for obs in self.obstacles:

            r = obs.get_collision_radius()
            p = obs.get_position()
            ap = (p[0]-a[0],p[1]-a[1])
            
            fraction = self.dot(ab,ap) / ab_sqrMag

            if(fraction > 1):
                fraction = 1
            elif(fraction < 0):
                fraction = 0
                
            # find closest point Q on line AB
            qx = a[0] + fraction*ab[0]
            qy = a[1] + fraction*ab[1]
            
            # compute sqr distance Q to P
            dx = p[0] - qx
            dy = p[1] - qy
            sqrDist = (dx*dx)+(dy*dy)
            sqrRadius = r*r
            
            # check if the circle intersects the line
            if(sqrDist < sqrRadius):
                # is this a closer hit than before?
                if(fraction < frc):
                    closest = obs
                    frc = fraction

        return closest

        

    def dot(self,a,b):
        return ((a[0]*b[0])+(a[1]*b[1]))
        
    def sqrMag(self,v):
        return ((v[0]*v[0]) + (v[1]*v[1]))
