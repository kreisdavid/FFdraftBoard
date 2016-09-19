from graphics import *

class Button:
    def __init__(self, graphWindow, center, width, height, label, bColor):
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin,self.ymin)
        p2 = Point(self.xmax,self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill(bColor)
        self.rect.draw(graphWindow)
        self.label = Text(center, label)
        self.label.draw(graphWindow)
        self.deactivate()

    def getLabel(self):
        return self.label.getText()

    def deactivate(self):
        self.label.setFill('darkgray')
        self.rect.setWidth(1)
        self.active = False

    def activate(self):
        self.label.setFill('black')
        self.rect.setWidth(1)
        self.active = True

    def check(self,point):
        if self.active:
            if point.getX()>self.xmin and point.getX()<self.xmax:
                if point.getY()>self.ymin and point.getY()<self.ymax:
                    return True
        else:
            return False

def fourteenTeamLeague(draftWindow):
    clear = Rectangle(Point(0,0),Point(1300,650))
    clear.draw(draftWindow)
    clear.setFill('white')

    """
    #lol, what am i doing
    clear = Rectangle(Point(0,0),Point(1300,650))
    clear.draw(teamWindow)
    clear.setFill('white')
    
    #clears the previous selection screen
    """

    
    rd1 = Text(Point(50,585),'Round 1')
    rd1.setSize(13)
    rd1.draw(draftWindow)
    rd2 = Text(Point(50,548.072),'Round 2')
    rd2.setSize(13)
    rd2.draw(draftWindow)
    rd3 = Text(Point(50,511.144),'Round 3')
    rd3.setSize(13)
    rd3.draw(draftWindow)
    rd4 = Text(Point(50,474.216),'Round 4')
    rd4.setSize(13)
    rd4.draw(draftWindow)
    rd5 = Text(Point(50,437.288),'Round 5')
    rd5.setSize(13)
    rd5.draw(draftWindow)
    rd6 = Text(Point(50,400.36),'Round 6')
    rd6.setSize(13)
    rd6.draw(draftWindow)
    rd7 = Text(Point(50,363.432),'Round 7')
    rd7.setSize(13)
    rd7.draw(draftWindow)
    rd8 = Text(Point(50,326.504),'Round 8')
    rd8.setSize(13)
    rd8.draw(draftWindow)
    rd9 = Text(Point(50,289.576),'Round 9')
    rd9.setSize(13)
    rd9.draw(draftWindow)
    rd10 = Text(Point(50,252.648),'Round 10')
    rd10.setSize(13)
    rd10.draw(draftWindow)
    rd11 = Text(Point(50,215.72),'Round 11')
    rd11.setSize(13)
    rd11.draw(draftWindow)
    rd12 = Text(Point(50,178.792),'Round 12')
    rd12.setSize(13)
    rd12.draw(draftWindow)
    rd13 = Text(Point(50,141.864),'Round 13')
    rd13.setSize(13)
    rd13.draw(draftWindow)
    rd14 = Text(Point(50,104.936),'Round 14')
    rd14.setSize(13)
    rd14.draw(draftWindow)
    rd15 = Text(Point(50,68.008),'Round 15')
    rd15.setSize(13)
    rd15.draw(draftWindow)

    """
    #agghh, so ineficient, but works for team window
    rd1 = Text(Point(50,585),'QB')
    rd1.setSize(13)
    rd1.draw(teamWindow)
    rd2 = Text(Point(50,548.072),'RB')
    rd2.setSize(13)
    rd2.draw(teamWindow)
    rd3 = Text(Point(50,511.144),'RB')
    rd3.setSize(13)
    rd3.draw(teamWindow)
    rd4 = Text(Point(50,474.216),'WR')
    rd4.setSize(13)
    rd4.draw(teamWindow)
    rd5 = Text(Point(50,437.288),'WR')
    rd5.setSize(13)
    rd5.draw(teamWindow)
    rd6 = Text(Point(50,400.36),'TE')
    rd6.setSize(13)
    rd6.draw(teamWindow)
    rd7 = Text(Point(50,363.432),'FLEX')
    rd7.setSize(13)
    rd7.draw(teamWindow)
    rd8 = Text(Point(50,326.504),'K')
    rd8.setSize(13)
    rd8.draw(teamWindow)
    rd9 = Text(Point(50,289.576),'DST')
    rd9.setSize(13)
    rd9.draw(teamWindow)
    rd10 = Text(Point(50,252.648),'Bench')
    rd10.setSize(13)
    rd10.draw(teamWindow)
    rd11 = Text(Point(50,215.72),'Bench')
    rd11.setSize(13)
    rd11.draw(teamWindow)
    rd12 = Text(Point(50,178.792),'Bench')
    rd12.setSize(13)
    rd12.draw(teamWindow)
    rd13 = Text(Point(50,141.864),'Bench')
    rd13.setSize(13)
    rd13.draw(teamWindow)
    rd14 = Text(Point(50,104.936),'Bench')
    rd14.setSize(13)
    rd14.draw(teamWindow)
    rd15 = Text(Point(50,68.008),'Bench')
    rd15.setSize(13)
    rd15.draw(teamWindow)
    """

    for x in range(15):
        line = Line(Point(135+(x*80.357),46.08), Point(135+(x*80.357),650))
        line.draw(draftWindow)
        #line = Line(Point(135+(x*80.357),46.08), Point(135+(x*80.357),650))
        #line.draw(teamWindow)
    for y in range(16):
        h = Line(Point(0,600-(y*36.928)), Point(1259.998,600-(y*36.928)))
        h.draw(draftWindow)
        #h = Line(Point(0,600-(y*36.928)), Point(1259.998,600-(y*36.928)))
        #h.draw(teamWindow)
        #so much shitty programming
        

    #button to submit team name
    submit = Button(draftWindow,Point(800,25),75,22,'Submit','red')
    submit.activate()

    #the number of the team
    tNum = 1

    while tNum < 15:
        
        #text to prompt user to enter the team names
        prompt = Text(Point(525,25),'Enter Team '+str(tNum))
        prompt.setSize(14)
        prompt.draw(draftWindow)
        
        #input window for entering the names
        tNameInput = Entry(Point(675,25),15)
        tNameInput.draw(draftWindow)
        
        c = draftWindow.getMouse()
        while not submit.check(c):
            c = draftWindow.getMouse()
        #lol, here comes more shitty programming
        if tNum == 1:
            t1 = Text(Point(175,625),tNameInput.getText())
            t1.setSize(12)
            t1.draw(draftWindow)
            #t1 = Text(Point(175,625),tNameInput.getText())
            #t1.setSize(12)
            #t1.draw(teamWindow)
        elif tNum == 2:
            t2 = Text(Point(250.357,625),tNameInput.getText())
            t2.setSize(12)
            t2.draw(draftWindow)
            #t2 = Text(Point(250.357,625),tNameInput.getText())
            #t2.setSize(12)
            #t2.draw(teamWindow)
        elif tNum == 3:
            t3 = Text(Point(330.714,625),tNameInput.getText())
            t3.setSize(12)
            t3.draw(draftWindow)
            #t3 = Text(Point(330.714,625),tNameInput.getText())
            #t3.setSize(12)
            #t3.draw(teamWindow)
        elif tNum == 4:
            t4 = Text(Point(411.071,625),tNameInput.getText())
            t4.setSize(12)
            t4.draw(draftWindow)
            #t4 = Text(Point(411.071,625),tNameInput.getText())
            #t4.setSize(12)
            #t4.draw(teamWindow)
        elif tNum == 5:
            t5 = Text(Point(491.428,625),tNameInput.getText())
            t5.setSize(12)
            t5.draw(draftWindow)
            #t5 = Text(Point(491.428,625),tNameInput.getText())
            #t5.setSize(12)
            #t5.draw(teamWindow)
        elif tNum == 6:
            t6 = Text(Point(571.785,625),tNameInput.getText())
            t6.setSize(12)
            t6.draw(draftWindow)
            #t6 = Text(Point(571.785,625),tNameInput.getText())
            #t6.setSize(12)
            #t6.draw(teamWindow)
        elif tNum == 7:
            t7 = Text(Point(652.142,625),tNameInput.getText())
            t7.setSize(12)
            t7.draw(draftWindow)
            #t7 = Text(Point(652.142,625),tNameInput.getText())
            #t7.setSize(12)
            #t7.draw(teamWindow)
        elif tNum == 8:
            t8 = Text(Point(732.499,625),tNameInput.getText())
            t8.setSize(12)
            t8.draw(draftWindow)
            #t8 = Text(Point(732.499,625),tNameInput.getText())
            #t8.setSize(12)
            #t8.draw(teamWindow)
        elif tNum == 9:
            t8 = Text(Point(812.856,625),tNameInput.getText())
            t8.setSize(12)
            t8.draw(draftWindow)
            #t8 = Text(Point(812.856,625),tNameInput.getText())
            #t8.setSize(12)
            #t8.draw(teamWindow)
        elif tNum == 10:
            t8 = Text(Point(893.213,625),tNameInput.getText())
            t8.setSize(12)
            t8.draw(draftWindow)
            #t8 = Text(Point(893.213,625),tNameInput.getText())
            #t8.setSize(12)
            #t8.draw(teamWindow)
        elif tNum == 11:
            t8 = Text(Point(973.57,625),tNameInput.getText())
            t8.setSize(12)
            t8.draw(draftWindow)
            #t8 = Text(Point(973.57,625),tNameInput.getText())
            #t8.setSize(12)
            #t8.draw(teamWindow)
        elif tNum == 12:
            t8 = Text(Point(1053.927,625),tNameInput.getText())
            t8.setSize(12)
            t8.draw(draftWindow)
            #t8 = Text(Point(1053.927,625),tNameInput.getText())
            #t8.setSize(12)
            #t8.draw(teamWindow)
        elif tNum == 13:
            t8 = Text(Point(1134.284,625),tNameInput.getText())
            t8.setSize(12)
            t8.draw(draftWindow)
            #t8 = Text(Point(1134.284,625),tNameInput.getText())
            #t8.setSize(12)
            #t8.draw(teamWindow)
        elif tNum == 14:
            t8 = Text(Point(1214.641,625),tNameInput.getText())
            t8.setSize(12)
            t8.draw(draftWindow)
            #t8 = Text(Point(1214.641,625),tNameInput.getText())
            #t8.setSize(12)
            #t8.draw(teamWindow)
            
            
        prompt.undraw()
        tNum += 1

   

    prompt = Text(Point(425,25),"Enter Player Position and Name")
    prompt.setSize(13)
    prompt.draw(draftWindow)

    pick = 1
    roundNum = 1

    while roundNum < 16: #number of pick in the draft will be 210
        tNameInput = Entry(Point(675,25),15)
        tNameInput.draw(draftWindow)
        #for player name

        #for player position
        pInput = Entry(Point(575,25),5)
        pInput.draw(draftWindow)
        c = draftWindow.getMouse()
        while not submit.check(c):
            c = draftWindow.getMouse()
        pPosition = pInput.getText()
        pName = tNameInput.getText()
        if pPosition == 'QB':
            pcolor = 'orange'
        elif pPosition == 'RB':
            pcolor = 'lightblue'
        elif pPosition == 'WR':
            pcolor = 'lightgreen'
        elif pPosition == 'TE':
            pcolor = 'pink'
        elif pPosition == 'K':
            pcolor = 'yellow'
        elif pPosition == 'DEF':
            pcolor = 'brown'
        elif pPosition == 'NA':
            pcolor = 'black'

        #here is where we need some demensions and to make the picks
            #snake back and fourth between the rounds
        if roundNum%2 == 1:
            placePick = Button(draftWindow,Point(175.1785+((pick-1)*80.357),581.536-((roundNum-1)*36.928)),80.357,36.928,pName,pcolor)
            placePick.activate()
        else:
            placePick = Button(draftWindow,Point((175.1785+(13*80.357))-((pick-1)*80.357),581.536-((roundNum-1)*36.928)),80.357,36.928,pName,pcolor)
            placePick.activate()

        pick = pick+1
        if pick == 15:
            pick = 1
            roundNum = roundNum + 1
                           

def main():

    #wnx = GraphWin("Teams by Positions",1300,650)
    #wnx.setCoords(0,0,1300,650)

    parameterWindow = GraphWin("Draft Board", 500, 500)
    parameterWindow.setCoords(0,0,500,500)
    parameterWindow.setBackground('lightblue')

    instructions = Text(Point(250, 375), "Enter league information:")
    instructions.setSize(30)
    instructions.draw(parameterWindow)
    # fix formatting for parameter window, still looks funny
    teamText = Text(Point(175, 250), "# Teams")
    teamText.setSize(20)
    teamText.draw(parameterWindow)

    teamInput = Entry(Point(275, 250), 7)
    teamInput.draw(parameterWindow)

    roundsText = Text(Point(175, 200), "# Rounds")
    roundsText.setSize(20)
    roundsText.draw(parameterWindow)

    roundInput = Entry(Point(275, 200), 7)
    roundInput.draw(parameterWindow)

    """
    #button to submit team name
    submit = Button(draftWindow,Point(800,25),75,22,'Submit','red')
    submit.activate()

    
        #input window for entering the names
        tNameInput = Entry(Point(675,25),15)
        tNameInput.draw(draftWindow)
        
        c = draftWindow.getMouse()
        while not submit.check(c):
            c = draftWindow.getMouse()


    """
    

    wn = GraphWin("Fantasy Football Draft", 1300,650)
    wn.setCoords(0,0,1300,650)
    wn.setBackground('lightblue')
    #creates window to fill screen
    
    #buttons for different size league selection
    teams8 = Button(wn,Point(260,325),100,100,'8','orange')
    teams8.activate()
    teams10 = Button(wn,Point(520,325),100,100,'10','orange')
    teams10.activate()
    teams12 = Button(wn,Point(780,325),100,100,'12','orange')
    teams12.activate()
    teams14 = Button(wn,Point(1040,325),100,100,'14','orange')
    teams14.activate()

    #asks how many teams over displayed buttons
    askTeams = Text(Point(650,487.5),"How many teams in the league?")
    askTeams.setSize(25)
    askTeams.draw(wn)

    selected = False
    pt = wn.getMouse()
    while not selected: # remember to change selected to true when selected
        if teams8.check(pt):
            pass
            #eightTeamLeague(wn,wnx)
        elif teams10.check(pt):
            pass
            #tenTeamLeague(wn,wnx)
        elif teams12.check(pt):
            pass
            #twelveTeamLeague(wn,wnx)
        elif teams14.check(pt):
            fourteenTeamLeague(wn) #add wnx if i ever decide to get that to work again
        pt = wn.getMouse()

    

    wn.close()
    wnx.close()
main()
