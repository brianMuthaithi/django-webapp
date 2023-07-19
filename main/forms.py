from django import forms
from .models import BikeModel, BranchModel, RouteModel, CustomerModel, Return_bike


bike_condition = [('Issuable', 'Issuable'), ('In-Repair', 'In-Repair')]

class RegCustomer(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Enter full name'}))
    tel = forms.IntegerField(label="Telephone Number", widget=forms.TextInput(attrs={'placeholder': 'Tel No.'}))
    bike = forms.ModelChoiceField(queryset=BikeModel.objects.all(), label="Bike")
    route = forms.ModelChoiceField(queryset=RouteModel.objects.all(), label="Route")
    branch= forms.ModelChoiceField(queryset=BranchModel.objects.all(), label="Branch")
    time = forms.DateTimeField(label="Departure Time", widget=forms.DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM'}))

    class Meta:
        model = CustomerModel
        fields = ['name', 'tel', 'bike', 'branch', 'route', 'time']


class RegBike(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter full name'}), max_length=200)
    type = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Bike Type'}), max_length=200)
    wheels = forms.IntegerField(label="Wheels", min_value=1, max_value=4)
    weight = forms.FloatField(label="Weight", widget=forms.TextInput(attrs={'placeholder': 'Weight(kgs)'}))
    material = forms.CharField(label="Frame Material", max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Chasis material'}))
    condition = forms.CharField(label="Condition", widget=forms.Select(choices=bike_condition))

    class Meta:
        model = BikeModel
        fields = ['name', 'type', 'wheels', 'weight', 'material', 'condition']


class RegRoute(forms.Form):
    name = forms.CharField(label="Route Name", max_length=200)
    route_type = forms.CharField(label="Route Type", max_length=200)
    length = forms.FloatField(label="Distance_km")
    date = forms.DateField(label="Date")
    weather = forms.CharField(label="Weather", max_length=200)

    class Meta:
        model = RouteModel
        fields = ['name', 'route_type', 'length', 'date', 'weather']


class RegBranch(forms.Form):
    name = forms.CharField(label="Branch Name", max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    manager = forms.CharField(label="Branch Manager", max_length=200, widget=forms.TextInput(attrs={'placeholder': "Manager's name"}))

    class Meta:
        model = BranchModel
        fields = ['name', 'manager']


class Return_form(forms.Form):
    customer_id = forms.ModelChoiceField(queryset=CustomerModel.objects.all(), label="Customer ID")
    bike_id = forms.ModelChoiceField(queryset=BikeModel.objects.all(), label="Bike ID")
    branch_id = forms.ModelChoiceField(queryset=BranchModel.objects.all(), label="Branch ID")
    return_time = forms.DateTimeField(label="Return Time")

    class Meta:
        model = Return_bike
        fields = ['customer_id', 'bike_id', 'branch_id', 'return_time']

