/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: Emre Guzel
 * Created on: Oct 1 2024
 * This program is cocike cilcker 
*/

//basic.showString('Hello, World!')
basic.clearScreen()
let cocikeNumber=+1
let cocikeRest=0
basic.showIcon(IconNames.Happy)
input.onButtonPressed(Button.B,function(){
    cocikeRest=0
    basic.showNumber(0)
})
input.onButtonPressed(Button.A,function(){
 cocikeNumber += 1
 basic.showNumber(1)
})


