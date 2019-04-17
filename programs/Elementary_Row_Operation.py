class ElementaryRawOpeartion():
    def __init__(self,x1,y1,x,x2,y2,y):
        #for Row 1
        self.x1 = x1 = float(x1)
        self.y1 = y1 = float(y1)
        self.x = x = float(x)

        #for Row 2
        self.x2 = x2 = float(x2) 
        self.y2 = y2 = float(y2)
        self.y = y = float(y)

    def all_steps(self):
        #Step 1: Makng 1st element of R1 == 1 by xing by its inverse with R1.
        self.y2 *= (1/self.x1)
        self.x *= (1/self.x1)
        self.x1 *= (1/self.x1)

        #Step 2: Making 1st element of R2 == 0
        """To save actual values form manupulating; x_1, y_1, _x """
        x_1 = self.x1 
        y_1 = self.y1
        _x = self.x
        
        _x2 = self.x2 
        if (_x2 >= 0): _x2 *= -1
        # R1 * _x2
        x_1 *= _x2
        y_1 *= _x2
        _x *= _x2

        # R1 * _x2 + R2
        self.x2 += x_1
        self.y2 += y_1
        self.y += _x

        #Step 3: Making 2nd element of R2 == 1 by xing by its invese with R2. 
        self.x2 *= (1/self.y2)
        self.y *= (1/self.y2)
        self.y2 *= (1/self.y2)

        #Step 4: Making 2nd element of R1 == 0; by 
        """To save actual values form manupulating; x_2, y_2, _y """
        x_2 = self.x2
        y_2 = self.y2
        _y = self.y

        _y1 = self.y1
        if (_y1 >= 0): _y1 *= -1
        else: _y1 *= -1

        # R2 * _y1
        x_2 *= _y1 
        y_2 *= _y1
        _y *= _y1

        #R2 * _y1 + R1
        self.x1 += x_2
        self.y1 += y_2
        self.x += _y

        print('\n| x1  y1 : x |' + ' == ' + '| ', self.x1, '   ' ,  self.y1, ' : ', self.x, '   |' +
              '\n| x2  y2 : y |' + ' == ' + '| ', self.x2, '   ' ,  self.y2, ' : ', self.y, ' |')


        return self.x1, self.y1, self.x2, self.y2, self.x, self.y

    def satisfaction(self,equation1='',equation2=''):
        a = self.x
        b = self.y
        calling = ElementaryRawOpeartion.all_steps(self)
        x = self.x
        y = self.y 

        if equation1:
            equation1 = int(eval(equation1))
            print(equation1, '=', int(a))
        if equation2:
            equation2 = int(eval(equation2))
            print(equation2, '=', int(b))

print('Enter numberes in augmented form: '+
      '\n| x1  y1 : x |'+
      '\n| x2  y2 : y |')

#R1
x1 = float(input('x1: ')) #2
y1 = float(input('y1: ')) # -5
x = float(input('x: ')) #3
#R2
x2 = float(input('x2: ')) #5
y2 = float(input('y2: ')) #13
y = float(input('y: ')) #8

print('/nEnter expression(s) without right hand side' + 
      '/nIf dont want to satisfy just leave it.')
equation1 = input('Enter equation1: ') #'2*x -5*y'
equation2 = input('Enter equation1: ') #'5*x + 13*y'


call = ElementaryRawOpeartion(x1,y1,x,x2,y2,y)
call.satisfaction(equation1, equation2)
call.all_steps()




		
