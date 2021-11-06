class Personal_information:  # 
    # The _ _init_ _ method initializes the attributes.
    def __init__(self, id, name, address, age, phonenumber):
        self.__id = id
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phonenumber = phonenumber


    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phonenumber(self, phonenumber):
        self.__phonenumber = phonenumber

    def set_id(self, id):
        self.__id = id



    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phonenumber(self):
        return self.__phonenumber

    def get_id(id):
        return self.__id




    def __str__(self):                              # attributes to show
        return 'Name: ' + str(self.__name) + \
            '\nAddress: ' + str(self.__address) + \
            '\nAge: ' + str(self.__age) + \
            '\nPhone_number: ' + str(self.__phonenumber)