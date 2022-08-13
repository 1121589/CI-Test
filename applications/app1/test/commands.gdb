target remote:1234
break water_level
c 100
set PINB=1
c 100
printf "\n PORTB=%d||Assert=2\n", PORTB
set PINB=0
c 100
printf "\n PORTB=%d||Assert=0\n", PORTB
quit
