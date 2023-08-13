from django.db import models


class Advertisement(models.Model):

    #Zagolovok
    #Небольшое текстовое поле
    title = models.CharField("Заголовок", max_length=128)

    #Описание

    #Большое текстовое поле
    description = models.TextField("Описание")

    #Цена
    #Число с фикс точкой
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)

    #Дата создания
    created_at = models.DateTimeField(auto_now_add=True)

    #Дата изменения
    updated_at = models.DateTimeField(auto_now=True)
    #Уместен ли торг
    auction = models.BooleanField("Торг", help_text="Отметьте, если хотите торговаться")
    
    def __str__(self):
        return f"Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price}"


    class Meta:
        db_table = "advertisements"
    
    #Изображение

    #Адрес

    #Отзывы/рейтинг продавца

    #Контакты продавца

    #Похожие товары

