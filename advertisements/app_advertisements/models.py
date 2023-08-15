from django.db import models
from django.contrib import admin
from django.utils.html import format_html

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
    
    @admin.display(description="Дата создания")
    def created_date(self):
        from django.utils import timezone

        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.strftime("%H:%M:%S")
            return format_html("<span style='color:green; font-weight:bold'> Сегодня в {}</span>", created_time)

        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")
    
    @admin.display(description="Дата обновления")
    def updated_date(self):
        from django.utils import timezone

        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.strftime("%H:%M:%S")
            return format_html("<span style='color:green; font-weight:bold'> Сегодня в {}</span>", updated_time)

        return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")
    

  


    def __str__(self):
        return f"Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price}"


    class Meta:
        db_table = "advertisements"
    
    #Изображение

    #Адрес

    #Отзывы/рейтинг продавца

    #Контакты продавца

    #Похожие товары

