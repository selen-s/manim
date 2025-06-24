from manim import *

def funnel(u, v):
            return np.array([.55 * np.cosh(u) * np.cos(v) , .55 * np.cosh(u) * np.sin(v) , .8*np.sinh(u)])

class vid(ThreeDScene):

    def construct(self):
        
        tex = Tex("loading").scale(1)
        d1 = Tex(".").scale(1)
        d2 = Tex(".").scale(1)
        d3 = Tex(".").scale(1)

        tex.shift(LEFT + UP)
        d1.shift(RIGHT + DOWN)
        d2.shift(RIGHT*2 + DOWN)
        d3.shift(RIGHT*3 + DOWN)

        tex2 = Tex("loading complete").scale(.5)
        
        c = Circle(fill_color=YELLOW) # create a circle

        s = Square() # create a square
        s.rotate(PI/2)

        tex.next_to(d1, LEFT, buff=0.4)

        self.play(Write(tex), run_time=.5)
        self.play(Write(d1), run_time =.1)
        self.play(Write(d2), run_time =.1)
        self.play(Write(d3), run_time =.1)

        for i in [1, 2, 3]:
                self.wait(.4)
                self.play(Blink(d1, time_on = .2, blinks = 1), run_time=.3)
                self.play(Blink(d2, time_on = .2, blinks = 1), run_time=.3)
                self.play(Blink(d3, time_on = .2, blinks = 1), run_time=.3)
        
        first = [ # loading screen
            FadeOut(tex, shift=LEFT, run_time=.5),
            FadeOut(d1, d2, d3, shift=LEFT, run_time=.5),
        ]
        self.play(AnimationGroup(*first), run_time=2)
        self.add(tex2)
        self.play(Blink(tex2, time_on = .8, blinks = 1), run_time = 1)
        self.remove(tex2)
        self.wait(1.5)
        
        #   shapes  #
        s.set_stroke(color=RED, width = 15)
        s.shift(RIGHT + UP)
        c.set_stroke(color = YELLOW, width = 9)
        c.set_fill(color=YELLOW, opacity=1)
        c.shift(LEFT*3)

        title = Tex("stormy day")
        self.play(Create(s), run_time = 1)
        self.play(Transform(s,c), run_time = 2)
        self.add(title)
        self.wait(1)

        c1 = "#3a4c5a" # dark 
        c2 = "#d6eef5" # light

        piece1 = Circle(stroke_color = c1, fill_color=c1, fill_opacity=1)
        piece2 = Circle(stroke_color = c1, fill_color=c1, fill_opacity=1)
        piece3 = Circle(stroke_color = c1, fill_color=c1, fill_opacity=1)
        piece2.shift(LEFT*.75)
        piece3.shift(LEFT*.5 + UP*.5)
        cloud = Group(piece1, piece2, piece3)
        self.add(cloud)
        cloud.shift(LEFT*10)

        p1 = Circle(stroke_color = c2, fill_color = c2, fill_opacity = 1)
        p2 = Circle(stroke_color = c2, fill_color = c2, fill_opacity = 1)
        p3 = Circle(stroke_color = c2, fill_color = c2, fill_opacity = 1)
        p2.shift(LEFT*.75)
        p3.shift(LEFT*.5 + UP*.5)
        cloud2 = Group(p1, p2, p3)
        cloud2.shift(LEFT*4)

        self.play(Transform(cloud, cloud2), run_time =2)
       
        bkg = Square(side_length=20, fill_color=' #33a0ff ', fill_opacity=1)
        bkg2 = Square(side_length=20, fill_color=BLACK, fill_opacity=1)
        self.play(SpinInFromNothing(bkg))
        self.play(Transform(bkg, bkg2))
        self.remove(bkg, bkg2, cloud, cloud2, title)
        self.remove(c, s)

        ## introduction is over
        ## actual animation begins
           
       
        axes = ThreeDAxes(x_range=[-10,10], x_length=20,
                          y_range=[-10,10], y_length=20,
                          z_range=[0, 10], z_length=10,
                            tips=True, 
                            color=BLACK)
        self.move_camera(phi= 75* DEGREES, theta = 30*DEGREES, run_time=2)
        self.add(axes)
        self.wait(.5)
        c3 = "#484E52"
        storm = Surface(
            lambda u, v: axes.c2p(*funnel(u,v)), 
            u_range=[-PI, PI], 
            v_range=[0,TAU], 
            fill_color = c3, 
            checkerboard_colors = (c3, c3),
            resolution=8)
        self.add(axes, storm)
        grp1 = Group(axes, storm)
        self.begin_ambient_camera_rotation(rate=.3, about="theta")
        self.wait(3)
        self.play(FadeOut(axes))
        
        tlabel = Tex("Cone Tornado")
        tlabel.shift(LEFT*4, UP)
        tmath1 = MathTex(r"x = a\cdot\cosh(u)\cdot\cos(v)")
        tmath2 = MathTex(r"y=b\cdot\cosh(u)\cdot\sin(v)")
        tmath3 = MathTex(r"z=c\cdot\sinh(u)")
        tmath1.shift(LEFT*4)
        tmath2.shift(LEFT*4, DOWN)
        tmath3.shift(LEFT*4, DOWN*2)

        texts = Group(tlabel, tmath1, tmath2, tmath3)
        texts.rotate_about_origin(3*PI/2, UP)
        texts.rotate_about_origin(PI/2, RIGHT)
        
        self.play(Write(tlabel, run_time=2))
        self.play(Write(tmath1, run_time=1))    
        self.play(Write(tmath2, run_time=1))
        self.play(Write(tmath3, run_time=1))            
        self.wait(4)

        self.play(Unwrite(tlabel, run_time = 1))
        self.play(Unwrite(tmath1, run_time=1))
        self.play(Unwrite(tmath2, run_time=1))
        self.play(Unwrite(tmath3, run_time=1))


        self.remove(storm)

        self.stop_ambient_camera_rotation()
        final = Tex("Selen's first manim project, 06/23/2025")
        final.rotate_about_origin(PI/4, UP)
        final.rotate_about_origin(PI/2, RIGHT)
        self.play(Write(final, run_time = 3))