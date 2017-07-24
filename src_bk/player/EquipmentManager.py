class Head:
    def __init__(self):
        self.overall = None
        self.nose = None
        self.mouth = None
        self.tongue = None
        self.ears = [None,None]
        self.neck = None
        self.eyes = None
        self.eyebrows = [None, None]

    def display(self):
        print("""
            Overall: {overall}
           _,------.__
          /        '  )      Eyebrows: {l_eyebrow}, {r_eyebrow}
         (__      ,-<@\      Eyes: {eyes}
         ((\           `-.   Nose: {nose}
          \Y   (     , '^<   Ears: {l_ear}, {r_ear}
          `-'   `   /   __\  Mouth: {mouth}
            | \     ,--'  (  Tongue: {tongue}
            |  `----------'
            |      |         Neck: {neck}""".format( 
                overall = self.overall ,
                l_eyebrow = self.eyebrows[0],
                r_eyebrow = self.eyebrows[1],
                eyes = self.eyes,
                nose = self.nose,
                l_ear = self.ears[0],
                r_ear = self.ears[1],
                mouth = self.mouth,
                tongue = self.tongue,
                neck = self.neck
                ))

class Arms:
    def __init__(self):
        self.grip = [None, None]
        self.fingers = [[None, None, None, None, None],[None, None, None, None, None]]

    def display(self):
        print("""
               Weilding: {hands[0]}, {hands[1]}
        ////                    Rings: {rings[0][0]}, 
       !!!!  _      \\\\\\\\               {rings[0][1]}, 
       !   -'/   _  ||||               {rings[0][2]}, 
        \   /    \`-'''|               {rings[0][3]}, 
         \  |     \   /                {rings[0][4]}, 
         )  |      \  \ 
        /   |       \  \               {rings[1][0]}, 
                     \                 {rings[1][1]}, 
                                       {rings[1][2]}, 
                                       {rings[1][3]}, 
                                       {rings[1][4]}, 
            """.format(
                hands = self.grip,
                rings = self.fingers               
                ))

class Legs:
    def __init__(self):
        self.legs = None
        self.feet = None
    def display(self):
        print("""
             Legs: {legs}
     _                       _
    ( \\nnnn /  /  \  \ nnnn// )     
     (`    \  /    \  /    `)
      `-.   \/      \/   .-`
         `,  )      (  ,`
           ``        ``
           Feet: {feet}
            """.format(
                legs = self.legs,
                feet = self.feet
            )
        )
class Torso:
    def __init__(self):
        self.chest = None
        self.shoulders = None
        self.waist = None
        self.back = None
    def display(self):
        print("""
           Chest: {chest} 
                                          Shoulders: {shoulders} 
            __,--.__.--,__                  __,--.__.--,__
          .`              `.              .`              `.
        .`                  `.          .`                  `.
       /   /              \   \        /   /              \   \ 
            |            |                  |            | 
            |            |                  |            |  
            |            |                  |            |  
            |            |                  |            |  
            |            |                  |            |  
            |____________|                  |____________| 
        
        Waist: {waist}
                                           Back: {back}

            """.format(
                chest = self.chest,
                shoulders = self.shoulders,
                waist = self.waist,
                back = self.back
                ))

class Body:
    def __init__(self):
        self.head = Head()
        self.arms = Arms()
        self.torso = Torso()
        self.legs = Legs()

    def display(self):
        self.head.display()
        self.arms.display()
        self.torso.display()
        self.legs.display()

class EquipmentManager:

    def __init__(self):
        self.equipped = Body()
        # self.equipped.display()
        # quit()
