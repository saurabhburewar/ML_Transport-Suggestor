import util
import search
import airTravel
import railTravel
import dtree

def main():
    print("==========================================================================================")
    print(" ")
    print("\t\t\tWelcome to Transport Suggester")
    print(" ")
    print("==========================================================================================")
    print()
    print("Please enter source and destination")
    print()
    print("As of now you have 20 choices: ")
    print("Ahmedabad\tBangalore\tBhopal\t\tChennai\t\tDelhi")
    print("Hyderabad\tIndore\t\tJaipur\t\tKanpur\t\tKolkata")
    print("Lucknow\t\tLudhiana\tMumbai\t\tNagpur\t\tPatna")
    print("Pune\t\tSurat\t\tThane\t\tVadodara\tVisakhapatnam")
    print()
    src = str(input("Source: ").strip())
    print()
    dst = str(input("Destination: ").strip())
    print()
    print("Would you like to keep things environment-friendly?")
    print("\t For Yes, enter '1'")
    print("\t For No, enter '0'")
    env_conscious = int(input("Answer: ").strip())
    print()
    print("Want it cheap?")
    print("\t For Yes, enter '1'")
    print("\t For No, enter '0'")
    budget_conscious = int(input("Answer: ").strip())
    print()
    print("Is there anything you would like to avoid?")
    print("\t Avoid the roads: enter '0'")
    print("\t Avoid travel by air: enter '1'")
    print("\t Avoid railways: enter '2'")
    avoid = int(input("Answer: ").strip())
    
    util.Createcsv()
  
    dist = search.aStar(src, dst, "PrintDetails")
    airTravel.getAirDetails(src, dst)
    railTravel.getRailDetails(src, dst)
    print()
    dtree.predictDtree(dist, env_conscious ,budget_conscious ,avoid)
    print()
    print("==========================================================================================")
    print("\t\t\tHave a safe trip !!")
    print()


if __name__ == "__main__":
    main()