import turtle
from turtle import *
import pandas

screen  =Screen()
screen.title("US States Guessing Game")
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)



right_guess = 0

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
guessed_states = []

while right_guess <= 50:
    answer = screen.textinput(title="Guess the States", prompt=f'{right_guess}/50 Right')
    title_answer = answer.title()
    if title_answer == 'Exit':
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('Left Over States.csv')
        break

    check_answer = data[data['state'] == title_answer]

    if title_answer in all_states:
        guessed_states.append(title_answer)
        right_guess += 1
        write_turtle = Turtle()
        write_turtle.hideturtle()
        x_axis = check_answer['x']
        y_axis = check_answer['y']
        write_turtle.penup()
        write_turtle.goto(int(x_axis), int(y_axis))
        write_turtle.write(title_answer)









# screen.exitonclick()