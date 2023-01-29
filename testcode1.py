import streamlit as st

def get_zodiac_sign(year):
    zodiac_signs = {
        'rat': range(1900, 1912),
        'ox': range(1912, 1924),
        'tiger': range(1924, 1936),
        'rabbit': range(1936, 1948),
        'dragon': range(1948, 1960),
        'snake': range(1960, 1972),
        'horse': range(1972, 1984),
        'goat': range(1984, 1996),
        'monkey': range(1996, 2008),
        'rooster': range(2008, 2020),
        'dog': range(2020, 2032),
        'pig': range(2032, 2044)
    }
    for sign, years in zodiac_signs.items():
        if year in years:
            return sign
    return 'Invalid year'

def main():
    st.title("Chinese Zodiac Sign Finder")
    year = st.number_input("Enter your birth year:")
    zodiac_sign = get_zodiac_sign(year)
    st.success(f"Your Chinese zodiac sign is {zodiac_sign}.")

if __name__ == '__main__':
    main()
