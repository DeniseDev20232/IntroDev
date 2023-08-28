from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    
    def enter(self):
        print("This scene is not yet configured.") 
        print("Subclass it and implement enter().") 
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('foreverhome')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()


class LostDogStart(Scene):

    def enter(self):
        print(dedent("""
            Harry the Shaggy Pit Bull was abandoned! His bad people drove away on purpose                 because it was too expensive to feed him. 	Looking around, Harry sees a forest               behind him, a busy highway in fron to him, and down the road, a scary looking                 house.  Which does Harry choose to approach, forest, highway, or house?
            """))

        action = input("> ")

        if action == "forest":
            print(dedent("""
                Harry walks a little way into the forest. After about 15 minutes, he comes to                 a clearing. In the clearing, there is a family iof picnickers. They look                      really frightened! Harry follows their gaze and sees a bear.
                """))
            return 'bear'

        elif action == "highway":
            print(dedent("""
                There's a lot of traffic!
                """))
            return  'highway'

        elif action == "house":
            print(dedent("""
                The house looks abandoned, but as Harry gets closer, he smells something                      cooking, and a pack of dogs race out from behind the house, all barking at                    Harry!
                """))
            return  'dogpack'

        else:
            print(dedent("""
                Let's try this again, and see if you can follow directions this time?
                """))
            return 'lostdogstart'


class GratefulFamily(Scene):

    def enter(self):
        print(dedent("""
            The family is so excited that Harry chased away the bear! One of the kids runs up             and hugs Harry. Harry wants to lick her face, but Harry is hungry and sees their              food on the table. What to do? Lick the face or steal some hot dogs? Lick? Steal?             Steal? Lick?
            """))

        action = input("> ")

        if action == "lick":
            print(dedent("""
                They are excited that Harry is so friendly. They see he doesn't have a collar,                and takes him home at the end of the picnic. They take Harry to the vet, and he               is not chipped. The family advertises the found dog, but after 2 weeks, nobody                comes forward.
                """))
            return 'foreverhome'

        elif action == "steal":
            print(dedent("""
                Harry's stomach is full, but he's back where he started.
                """))
            return 'lostdogstart'

        else:
            print(dedent("""
                That wasn't an option. Try again!"
                """))
            return 'gratefulfamily'

class Bear(Scene):

    def enter(self):
        print(dedent("""
            The bear sees Harry and growls. What does Harry do? Fight or run ?
            """))
        action = input("> ")

        if action == "fight":
            print(dedent("""
                Harry charges at the bear. The bear is really surprised. It's never seen a                    shaggy pit bull before. It didn't wanta fight; it hoped to scare the people                   away and get some easy food. The bear turns around and runs into the forest.
                """))
            return 'gratefulfamily'

        elif action == "run":
            print(dedent("""
                You're back where you started.
                """))
            return 'lostdogstart'

        else:
            print(dedent("""
                That wasn't an option. Try again!
                """))
            return 'bear'

class FosterHome(Scene):

    def enter(self):
        print(dedent("""
            Harry gets very calm at his new foster family, but they ultimately decide to                  dopt him!
            """))
        return 'foreverhome'

class Veterinarian(Scene):

    def enter(self):
        print(dedent("""
            Fortunately, the driver who hit Harry stopped. Harry was unconscious but alive,               so the driver took him to the emergency vet. Harry woke up and had a couple of                bandages but was mostly fine, just a little sore. The vet cones in to check on                him. Does Harry act fearful or friendly?
            """))
        action = input("> ")

        if action == "fearful":
            print(dedent("""
                The veterinarian decides Harry is adoptable, but needs some  care and                         socialization first.
                """))
            return 'fosterhome'

        elif action == "friendly":
            print(dedent("""
                The vet is amazed by Harry's great disposition. Harry is sturdy and has a                     great disposition. If Harry's smart, too, he could make a big                                 difference in someone's life.
                """))
            return 'guidedog'

        else:
            print(dedent("""
                That wasn't an option. Try again!
                """))
            return 'veterinarian'

class Highway(Scene):

    def enter(self):
        print(dedent("""
            Maybe Harry should go carefully, and zigzag to avoid traffic. Or maybe it's                   better for him to just run straight across? Which path does Harry take, zigzag or             straight?
            """))
        action = input("> ")

        if action == "zigzag":
            print(dedent("""
                Haryy wasn't fast enough.
                """))
            return 'veterinarian'

        elif action == "straight":
            print(dedent("""
                Wow, Harry made it to the other side!
                """))
            return 'hitchhiker'

        else:
            print(dedent(""""
                That was not an option. Try again!
                """))
            return 'highway'


class GuideDog(Scene):

    def enter(self):
        print(dedent("""
            Harry went to guide dog school and did a great job! Now he is helping a blind                 18-year-old go away to college.
            """))
        return 'foreverhome'

class Hitchhiker(Scene):

    def enter(self):
        print(dedent("""
            On this side of the road, Harry sees a hitchhiker. He approaches the hitchhiker               slowly, and the hitchhiker offers him some food. He's impressed with how getly                Harry takes it and how freindly he is. He decides he has a new hitchhiking                    partner.
            """))
        return 'foreverhome'



class Homeowner(Scene):

    def enter(self):
        print(dedent("""
            How does Harry react to the owner? Friendly or timid?
            """))
        action = input("> ")

        if action == "friendly":
            print(dedent("""
                She decides that Harry would be a great addition to her pack!
                """))
            return 'foreverhome'

        elif action == "timid":
            print(dedent("""
                The homeowner realizes that a dog this gentle would be perfect for her                        granddaughter. She calls her, and the granddaughter drives up that weekend to                 pick him up and tak him home.
                """))
            return 'foreverhome'

        else:
            print(dedent(""""
                That was not an option. Try again!
                """))
            return 'homeowner'

class DogPack(Scene):

    def enter(self):
        print(dedent("""
            How does Harry react to the dogs? Does he Playbow or Run away? Type Bow or Run.
            """))
        action = input("> ")

        if action == "bow":
            print(dedent("""
                An older woman come sout of the house to see what all the noise is.
                """))
            return 'homeowner'

        elif action == "run":
            print(dedent("""
                Harry is going in circles!
                """))
            return 'lostdogstart'

        else:
            print(dedent(""""
                That was not an option. Try again!
                """))
            return 'dogpack'

class ForeverHome(Scene):

    quips = [
        "Harry has found his forever home!",
        "Harry has found his forever home!",

        ]

    def enter(self):
        print(ForeverHome.quips[randint(0, len(self.quips)-1)])
        exit(1)
        
        
class Map(object):

    scenes = {
        'lostdogstart': LostDogStart(),
        'gratefulfamily': GratefulFamily(),
        'bear': Bear(),
        'foaterhome': FosterHome(),
        'veterinarian': Veterinarian(),
        'guidedog': GuideDog(),
        'homeowner': Homeowner(),
        'hitchhiker': Hitchhiker(),
        'dogpack': DogPack(),
        'foreverhome': ForeverHome(),

    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('lostdogstart')
a_game = Engine(a_map)
a_game.play()