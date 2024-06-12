import turtle

def draw_bear():
    # 头部
    turtle.circle(50)

    # 耳朵
    turtle.right(30)
    turtle.forward(30)
    turtle.backward(30)
    turtle.left(60)
    turtle.forward(30)

    # 眼睛
    turtle.goto(20, 40)
    turtle.dot(5)
    turtle.goto(-20, 40)
    turtle.dot(5)

    # 鼻子
    turtle.goto(0, 20)
    turtle.dot(8)

    # 身体
    turtle.goto(0, -20)
    turtle.right(90)
    turtle.forward(50)

    # 腿
    turtle.right(45)
    turtle.forward(20)
    turtle.backward(20)
    turtle.left(90)
    turtle.forward(20)

    turtle.right(45)
    turtle.goto(0, -70)

    # 尾巴
    turtle.right(30)
    turtle.forward(15)

draw_bear()

turtle.done()
