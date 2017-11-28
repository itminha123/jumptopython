diamond = int(input("diamond: "))
for i in range(diamond*2):
     if i<=diamond:
          spaces = diamond - i
          stars = i
          print(" "*spaces + "* "*stars)
     else:
          spaces = i - diamond
          stars = 2*diamond - i
          print(" "*spaces + "* "*stars)







if (visit % 7) == 0 and visit < 22:
    Ticket=Ticket-1
    vip=vip-1
    print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 티켓 d%장" %Ticket)

    if ((visit % 7) == 0 and visit < 22) or ((visit % 3) == 0) and visit < 16:
         Ticket -= Ticket
         print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 티켓 d%장" % Ticket)
         vip -= vip
         print("축하 합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 d%장" % vip)