def filter_words(st):
    st = st.lower().capitalize().split()
    return ' '.join(st)


def main():
    print(filter_words('WOW this is REALLY amazing'))


if __name__ == '__main__':
    main()