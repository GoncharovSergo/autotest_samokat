import data
import sender_stand_request




#Меняем значение в теле запроса
def get_kit_body(name):
    new_kit_body = data.kit_body.copy()    #Копируется словарь с телом запроса из файла data
    new_kit_body["name"] = name            #Меняется значения в поле name
    return new_kit_body                    #Возвращается новый словарь с нужным значением name




#Функция для позитивных проверок
def positive_assert(name):
    #В переменную kit_body сохраняется новое тело запроса
    kit_body = get_kit_body(name)
    #В переменную kit_respons сохраняется результат запроса на создание набора
    kit_response = sender_stand_request.post_new_client_kit(kit_body, sender_stand_request.auth_token)
    #Проверка, что в ответе есть поле name и оно не пустое
    assert kit_response.json()["name"] == name
    #Проверка, что код ответа равен 201
    assert kit_response.status_code == 201




#Функция для негативных проверок
def negative_assert_code_400(name):
    #В переменную kit_body_negative сохраняется новое тело запроса
    kit_body_negative = get_kit_body(name)
    #В переменную kit_response сохраняется результат запроса на создание набора
    kit_response = sender_stand_request.post_new_client_kit(kit_body_negative, sender_stand_request.auth_token)
    #Проверка, что код ответа равен 400
    assert kit_response.status_code == 400




#Позитивные провернки

#Тест 1 Проверка допустимого количества символов (1)
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")

#Тест 2 Проверка допустимого количества символов (511)
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                    "dabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcd"
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                    "abcdabcdabcdabcdabcdabcdabcdabcdabC")

#Тест 3 Проверка допустимых символов (английские буквы)
def test_create_kit_english_letters_in_name_get_success_response():
    positive_assert("QWErty")

#Тест 4 Проверка допустимых символов (русские буквы)
def test_create_kit_russian_letters_in_name_get_success_response():
    positive_assert("Мария")

#Тест 5 Проверка допустимых символов (спецсимволы)
def test_create_kit_has_special_sym_in_name_get_success_response():
    positive_assert('"№%@",')

#Тест 6 Проверка допустимых символов (пробелы)
def test_create_kit_has_space_in_name_get_success_response():
    positive_assert(" Человек и КО ")

#Тест 7 Проверка допустимых символов (цифры)
def test_create_kit_numbers_in_name_get_success_response():
    positive_assert("123")




#Негативные проверки

#Тест 8 Проверка недопустимых символов (пустая строка)
def test_create_kit_0_letter_in_name_get_error_response():
    negative_assert_code_400("")

#Тест 9 Проверка допустимого количества символов (512)
def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert_code_400("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                             "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                             "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                             "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcd"
                             "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                             "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                             "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                             "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

#Тест 10 Параметр не передан в запросе
def test_create_kit_no_name_get_error_response():
    negative_assert_code_400(None)

#Тест 11 Передан другой тип параметра (число)
def test_create_kit_numbers_in_name_get_error_response():
    negative_assert_code_400("123")