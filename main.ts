input.onButtonPressed(Button.A, function () {
    switch (step) {
        case 1:
            num1 += 1
            basic.showString("" + (num1))
            break
        case 2:
            num2 += 1
            basic.showString("" + num2)
            break;
        case 3:
            op += 1
            sign()
    }
})
input.onButtonPressed(Button.AB, function () {
    switch(step){
        case 1:
            basic.clearScreen()
            step=2
            break
        case 2:
            basic.clearScreen()
            step=3
            break
            case 3:

    
    switch(op){
              case 1:
              answer= num1+num2
            basic.showString("" + answer)
            break
            case 2:
            answer=num1-num2
            basic.showString("" + answer)
            break
            case 3:
            answer=num1*num2
            basic.showString("" + answer)
            case 4:
            answer=num1/num2
            basic.showString("" + answer)
          }
          basic.pause(5000)
          control.reset()
    }
})
input.onButtonPressed(Button.B, function () {
    switch (step) {
        case 1:
            num1 += -1
            basic.showString("" + (num1))
            break
        case 2:
            num2 += -1
            basic.showString("" + num2)
            break;
        case 3:
            op += -1
            sign()
    }
})
function sign () {
    if (op == 1) {
        basic.showLeds(`
            . . # . .
            . . # . .
            # # # # #
            . . # . .
            . . # . .
            `)
    } else if (op == 2) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . # # # .
            . . . . .
            . . . . .
            `)
    } else if (op == 3) {
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            `)
    } else if (op == 4) {
        basic.showLeds(`
            . . # . .
            . . . . .
            # # # # #
            . . . . .
            . . # . .
            `)
    } else if (op == 0) {
    	
    } else {
        op = 4
    }
}
let in_num = 0
let op = 0
let num2 = 0
let num1 = 0
let step = 1
let answer=0
