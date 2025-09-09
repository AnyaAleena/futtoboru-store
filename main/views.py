from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama_app' : 'Futtoboru Store',
        'nama_mhs': 'Anya Aleena Wardhany',
        'npm': '2406401773',
        'kelas' : 'PBP B'
    }

    return render(request, "main.html", context)