
import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--type', type=str)
parser.add_argument('--principal', type=int)
parser.add_argument('--interest', help="interest", type=float)
parser.add_argument('--periods', type=int)
parser.add_argument('--payment', type=int)
args = parser.parse_args()

if args.interest is None:
    print('Incorrect parameters')
else:
    months = 1
    total_pay = 0
    nominal_rate = args.interest / (12 * 100)
    if  args.type == "diff":


        for payment_m in range(args.periods):   
            payment_m = math.ceil((args.principal / args.periods) + nominal_rate * (args.principal - ((args.principal * (months - 1.0) / args.periods))))
            print('Month ' + str(months) + ': payment is ' + str(payment_m) + '.')
            total_pay += payment_m
            months += 1
            if months > args.periods:
                print('\nOverpayment = ', total_pay - args.principal)
                break

    else:

        if args.principal is None:
            principal = ((nominal_rate * math.pow((1 + nominal_rate), args.periods)) / (math.pow((1 + nominal_rate), args.periods) - 1))
            principal1 = round(args.payment / principal)
            print("Your credit principal = {}!".format(principal1))
            
            print('Overpayment', args.periods * args.payment - principal1)
        elif args.periods == None:

            periods = round(math.log(args.payment / (args.payment - nominal_rate * args.principal), (1 + nominal_rate)))
            count = round(periods // 12)
            count_m = math.ceil(periods % 12)
            if count_m == 0:
                print("It will take {}".format(count), "to repay this credit!")
            else:
                print("You need {} years".format(count), "and {} months to repay this credit!".format(count_m))
            print('Overpayment', (args.payment * periods) - args.principal)
        else:
            annuity_pay = (math.ceil(args.principal * (nominal_rate * math.pow((1 + nominal_rate),args.periods))/(math.pow((1 + nominal_rate), args.periods) - 1)))
            print("Tour annuity payment = {}!".format(annuity_pay))
            print('Overpayment', annuity_pay * args.periods - args.principal)


