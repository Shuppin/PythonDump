from manim import *

class CircleFromPointsExample(Scene):
    def construct(self):

        number_plane = NumberPlane(
            x_range=(-10,10,1),
            y_range=(-10,10,1),
            x_length=10,
            y_length=10,
            background_line_style={
                "stroke_width": 1,
            }
        )

        circle = Circle.from_three_points(LEFT*2 + DOWN, LEFT*2.5, RIGHT*2+DOWN, color=RED)
        dots = VGroup(
            Dot(LEFT*2 + DOWN, color=RED),
            Dot(LEFT*2.5, color=RED),
            Dot(RIGHT*2 + DOWN, color=RED),
        )

        line1 = Line(dots[2], dots[0])
        arrow = Arrow(dots[0], dots[1], buff=0)

        line2 = Line(dots[2], UP*2.25+RIGHT*2, stroke_width=1)
        line3 = Line(LEFT*2.5, UP*2.25+RIGHT*2, stroke_width=1)

        l2l3_intersect = Dot(UP*2.25+RIGHT*2, color=GRAY)

        origin = Dot(UP*0.625, color=BLUE)

        line4 = Line(l2l3_intersect, origin, stroke_width=1)
        line4_higlight = Line(l2l3_intersect, origin, stroke_width=2, color=YELLOW)
        line5 = Line(dots[0], origin, stroke_width=1)
        line5_higlight = Line(origin, dots[0], stroke_width=2, color=YELLOW)

        arrowline5 = Arrow(origin, dots[0], buff=0)

        mathtext = VGroup(
            MathTex("L_1", color=BLUE_B).scale(1),
            MathTex("=", color=BLUE_B).scale(1).shift(RIGHT*0.6),
            MathTex("L_2", color=BLUE_B).scale(1).shift(RIGHT*1.2)
        )
        mathtext2 = VGroup(
            MathTex("=", color=BLUE_B).scale(1).shift(RIGHT*1.8),
            MathTex("r", color=BLUE_B).scale(1).shift(RIGHT*2.25)
        )
        mathtext.shift(LEFT*4 + UP*3)
        mathtext2.shift(LEFT*4 + UP*3)

        self.add(number_plane)
        self.add(Text("Circle from 3 Points Demo", color=BLUE_C).scale(1).shift(DOWN*3.5))
        self.wait(1)
        self.play(Create(dots))
        self.wait(1)
        self.play(Create(line1))
        self.play(GrowArrow(arrow))
        self.wait(0.5)
        self.play(Create(line2), Create(line3), Create(l2l3_intersect), run_time = 2)
        self.wait(1)
        self.play(Create(origin), Create(line4), Create(line5), run_time = 1.5)
        self.play(Write(mathtext))
        self.play(Create(line4_higlight), run_time = 0.3)
        self.play(Indicate(mathtext[0]), run_time = 1.5)
        self.play(Uncreate(line4_higlight), run_time = 0.3)
        self.play(Create(line5_higlight), run_time = 0.3)
        self.play(Indicate(mathtext[2]), run_time = 1.5)
        self.play(Uncreate(line5_higlight), run_time = 0.3)
        self.wait(0.5)
        self.play(Create(circle))
        self.play(Create(arrowline5), Write(mathtext2))
        self.play(Indicate(arrowline5, scale_factor=1), Indicate(mathtext2[1]), run_time = 3)
        self.wait(0.2)
        self.play(Rotate(arrowline5, angle=2*PI, about_point=UP*0.625, rate_func=smooth), run_time = 2)
        self.wait(0.5)
        self.play(FadeOut(arrowline5), run_time = 2)
        self.wait(3)