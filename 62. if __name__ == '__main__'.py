import messages


print(__name__)
print(messages.__name__)

if __name__ == '__main__':  # allows modules to be used as standalone programs or imported as modules
    print("running this module directly")
else:
    print("running this module indirectly")
