def set_output(key, value):
    return f"::set-output name={key}::{value}"


def main():

    outputs = { "version": "1.0", "author": "Mickey Mouse"}
    
    for key, value in outputs.items():
        s = set_output(key, value)
        print(s)

if __name__ == "__main__":
    main()