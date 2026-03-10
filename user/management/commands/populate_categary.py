from user.models import categary
from django.core.management.base import BaseCommand

    
class Command(BaseCommand):
    help="this command inserts post data"
    
    def handle(self, *args, **options):
        categary.objects.all().delete()
        
        categories=['sports','eeducation','tech','food']
        

        for categary_name in categories :
            categary.objects.create(name=categary_name)
        
        self.stdout.write(self.style.SUCCESS("completed inserting data!"))        
    
            
    
    
    