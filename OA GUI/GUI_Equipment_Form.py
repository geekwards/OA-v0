try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

def create_equipment_form(parent):
    if parent == None:
        equipment_window = tk.Tk()
    else:
        equipment_window = tk.Toplevel(parent)
    
    equipment_form = GUI_equipment_form(equipment_window)
    return equipment_form,equipment_window

class GUI_equipment_form:
    weapon = ['Weapon']
    armor = ['Armor']
    extended = armor + weapon + ['Clothing','Misc Equipment','Container']
    cancel_click
    save_click
    close_click
    edit_click
    equip_type

    def set_edit(self):
        global cancel_click
        global save_click

        self.left_button.config(text='Cancel')
        self.left_button.config(command=self.cancel_click)
        self.right_button.config(text='Save')
        self.right_button.config(command=self.save_click)
        self.enable_form()

    def set_view(self):
        self.left_button.config(text='Close')
        self.left_button.config(command=self.close_click)
        self.right_button.config(text='Edit')
        self.right_button.config(command=self.edit_click)
        self.disable_form()

    def clear(self):
        self.f1.ename.delete(0,'end')
        self.f1.eshortdescription.delete(0,'end')
        self.f1.txtdescription.delete("1.0",'end')
        self.f1.ecost.delete(0,'end')
        self.f1.eweight.delete(0,'end')
        if self.equip_type in self.extended:
            self.f1.ehealth.delete(0,'end')
            self.f1.ecapacity.delete(0,'end')
            self.f1.especial.delete(0,'end')
        if self.equip_type in self.armor:
            self.f1.lstdefensetype.delete(0,'end')
        if self.equip_type in self.weapon:
            self.f1.ehands.delete(0,'end')
            self.f1.eweapontype.delete(0,'end')
            self.f1.erange.delete(0,'end')
            self.f1.eammotype.delete(0,'end')
            self.f1.lstdamagetype.delete(0,'end')

    def enable_form(self):
        for item in self.f1.winfo_children():
            item.config(state='normal')

    def disable_form(self):
        for item in self.f1.winfo_children():
            item.config(state='disabled')

    def configure_form(self,equipment_type):
        self.equip_type = equipment_type
        self.f1.destroy()
        self.f1 = tk.Frame(self.parent)
        self.f1.grid(sticky='nsew',row=2,column=0,padx=20,pady=20)
        self.f1.lblname = tk.Label(self.f1,text='Name')
        self.f1.lblname.grid(sticky='e',row=2,column=1,padx=5)
        self.f1.ename = tk.Entry(self.f1)
        self.f1.ename.grid(sticky='w',row=2,column=2,columnspan=3)
        self.f1.lblshortdescription = tk.Label(self.f1,text='Short Description')
        self.f1.lblshortdescription.grid(sticky='e',row=3,column=1,padx=5)
        self.f1.eshortdescription = tk.Entry(self.f1)
        self.f1.eshortdescription.grid(sticky='w',row=3,column=2,columnspan=3)
        self.f1.lbldescription = tk.Label(self.f1,text='Description')
        self.f1.lbldescription.grid(sticky='ne',row=4,column=1,padx=5)
        self.f1.txtdescription = tk.Text(self.f1,height=20,width=40)
        self.f1.txtdescription.grid(sticky='w',row=4,column=2,columnspan=3)
        self.f1.txtdescription.configure(wrap='word')
        self.f1.lblcost = tk.Label(self.f1,text='Cost')
        self.f1.lblcost.grid(sticky='e',row=5,column=1,padx=5)
        self.f1.lblweight = tk.Label(self.f1,text='Weight')
        self.f1.lblweight.grid(sticky='e',row=6,column=1,padx=5)
        self.f1.ecost = tk.Entry(self.f1)
        self.f1.ecost.grid(sticky='w',row=5,column=2)
        self.f1.eweight = tk.Entry(self.f1)
        self.f1.eweight.grid(sticky='w',row=6,column=2)
        if self.equipment_type in self.extended:
            self.f1.lblhealth = tk.Label(self.f1,text='Item Health')
            self.f1.lblhealth.grid(sticky='e',row=7,column=1,padx=5)
            self.f1.ehealth = tk.Entry(self.f1)
            self.f1.ehealth.grid(sticky='w',row=7,column=2)
            self.f1.lblcapacity = tk.Label(self.f1,text='Capacity')
            self.f1.lblcapacity.grid(sticky='e',row=8,column=1,padx=5)
            self.f1.ecapacity = tk.Entry(self.f1)
            self.f1.ecapacity.grid(sticky='w',row=8,column=2)
            self.f1.lblspecial = tk.Label(self.f1,text='Special Ability')
            self.f1.lblspecial.grid(sticky='e',row=9,column=1,padx=5)
            self.f1.especial = tk.Entry(self.f1)
            self.f1.especial.grid(sticky='w',row=9,column=2)
        if self.equip_type in self.armor:
            self.f1.lbldefensetype = tk.Label(self.f1,text='Defense')
            self.f1.lbldefensetype.grid(sticky='e',row=10,column=1,padx=5)
            self.f1.lstdefensetype = tk.Listbox(self.f1)
            self.f1.lstdefensetype.grid(sticky='w',row=10,column=2,columnspan=3)
        if self.equip_type in self.weapon:
            self.f1.lblcapacity.config(text='Ammo Capacity')
            self.f1.lblhands = tk.Label(self.f1,text='Hands to wield')
            self.f1.lblhands.grid(sticky='e',row=10,column=1,padx=5)
            self.f1.ehands = tk.Entry(self.f1)
            self.f1.ehands.grid(sticky='w',row=10,column=2)
            self.f1.lblweapontype = tk.Label(self.f1,text='Weapon Type')
            self.f1.lblweapontype.grid(sticky='e',row=11,column=1,padx=5)
            self.f1.eweapontype = tk.Entry(self.f1)
            self.f1.eweapontype.grid(sticky='w',row=11,column=2)
            self.f1.lblrange = tk.Label(self.f1,text='Range')
            self.f1.lblrange.grid(sticky='e',row=12,column=1,padx=5)
            self.f1.erange = tk.Entry(self.f1)
            self.f1.erange.grid(sticky='w',row=12,column=2)
            self.f1.lblammotype = tk.Label(self.f1,text='Ammo Type')
            self.f1.lblammotype.grid(sticky='e',row=13,column=1,padx=5)
            self.f1.eammotype = tk.Entry(self.f1)
            self.f1.eammotype.grid(sticky='w',row=13,column=2)
            self.f1.lbldamagetype = tk.Label(self.f1,text='Damage')
            self.f1.lbldamagetype.grid(sticky='e',row=14,column=1,padx=5)
            self.f1.lstdamagetype = tk.Listbox(self.f1)
            self.f1.lstdamagetype.grid(sticky='w',row=14,column=2,columnspan=3)
        self.f1.grid_columnconfigure(0,weight=1)
        self.f1.grid_columnconfigure(1,weight=3)
        self.f1.grid_columnconfigure(2,weight=3)
        self.f1.grid_columnconfigure(3,weight=1)
        self.f1.grid_columnconfigure(4,weight=3)
        self.f1.grid_columnconfigure(5,weight=3)
        self.f1.grid_columnconfigure(6,weight=1)

    def add_item(self,equipment_type,equipment,close_call,cancel_call,edit_call,save_call):
        self.close_click = close_call
        self.cancel_click = cancel_call
        self.edit_click = edit_call
        self.save_click = save_call

        self.enable_form()
        self.parent.title(equipment_type + ' - ' + equipment.name)
        self.lbltitle.config(text=equipment_type + ' - ' + equipment.name)
        self.clear()
        self.f1.ename.insert(0,equipment.name)
        self.f1.eshortdescription.insert(0,equipment.short_description)
        self.f1.txtdescription.insert('end',equipment.description)
        self.f1.ecost.insert(0,equipment.cost)
        self.f1.eweight.insert(0,equipment.weight)
        if self.equipment_type in self.extended:
            self.f1.ehealth.insert('end',equipment.health)
            self.f1.ecapacity.insert('end',equipment.capacity)
            self.f1.especial.insert('end',equipment.special)
        if self.equipment_type in self.armor:
            for d in equipment.damage_types:
                self.f1.lstdefensetype.insert(0,d.name.strip() + ': ' + d.short_description.strip())
        if self.equipment_type in self.weapon:
            self.f1.ehands.insert('end',equipment.hands)
            self.f1.eweapontype.insert('end',equipment.weapon_type)
            self.f1.erange.insert('end',equipment.range)
            self.f1.eammotype.insert('end',equipment.ammo_type)
            for d in equipment.damage_types:
                self.f1.lstdamagetype.insert(0,d.name.strip() + ': ' + d.short_description.strip())
        self.disable_form()

    def __init__(self,parent):
        self.parent = parent
        self.lbltitle = tk.Label(self.parent,text='EQUIPMENT NOT LOADED')
        self.lbltitle.grid(sticky='nsew',row=0,column=0,columnspan=6,rowspan=2,pady=20)
        self.f1 = tk.Frame(self.parent)
        self.f1.grid(sticky='nsew',row=2,column=0,padx=20,pady=20)
        self.f1.lblname = tk.Label(self.f1,text='Name')
        self.f1.lblname.grid(sticky='e',row=2,column=1,padx=5)
        self.f1.ename = tk.Entry(self.f1)
        self.f1.ename.grid(sticky='w',row=2,column=2,columnspan=3)
        self.f1.lblshortdescription = tk.Label(self.f1,text='Short Description')
        self.f1.lblshortdescription.grid(sticky='e',row=3,column=1,padx=5)
        self.f1.eshortdescription = tk.Entry(self.f1)
        self.f1.eshortdescription.grid(sticky='w',row=3,column=2,columnspan=3)
        self.f1.lbldescription = tk.Label(self.f1,text='Description')
        self.f1.lbldescription.grid(sticky='ne',row=4,column=1,padx=5)
        self.f1.txtdescription = tk.Text(self.f1,height=20,width=40)
        self.f1.txtdescription.grid(sticky='w',row=4,column=2,columnspan=3)
        self.f1.txtdescription.configure(wrap='word')
        self.f1.lblcost = tk.Label(self.f1,text='Cost')
        self.f1.lblcost.grid(sticky='e',row=5,column=1,padx=5)
        self.f1.lblweight = tk.Label(self.f1,text='Weight')
        self.f1.lblweight.grid(sticky='e',row=6,column=1,padx=5)
        self.f1.ecost = tk.Entry(self.f1)
        self.f1.ecost.grid(sticky='w',row=5,column=2)
        self.f1.eweight = tk.Entry(self.f1)
        self.f1.eweight.grid(sticky='w',row=6,column=2)
        self.f1.grid_columnconfigure(0,weight=1)
        self.f1.grid_columnconfigure(1,weight=3)
        self.f1.grid_columnconfigure(2,weight=3)
        self.f1.grid_columnconfigure(3,weight=1)
        self.f1.grid_columnconfigure(4,weight=3)
        self.f1.grid_columnconfigure(5,weight=3)
        self.f1.grid_columnconfigure(6,weight=1)
        self.left_button = tk.Button(self.parent,text='Close')
        self.left_button.config(width=10,height=2)
        self.left_button.grid(sticky='w',row=16,column=2,pady=10)
        self.right_button = tk.Button(self.parent,text='Edit')
        self.right_button.config(width=10,height=2)
        self.right_button.grid(sticky='w',row=16,column=4,pady=10)
