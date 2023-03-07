# vamos importar o módulo Tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from datetime import datetime
from tkinter import messagebox



# método que permite autenticar o usuário
def autenticar_usuario():

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    #teste#

    # vamos obter o valor da caixa de texto usuário
    usuario = txt_usuario.get()
    # vamos obter o valor da caixa de texto senha
    senha = txt_senha.get()
    # vamos testar se o nome de usuário e a senha estão corretos
    token = txt_token.get()
    # pegar qual shift
    shift = variable.get()

    janela_login.destroy()



#Autenticar página login

    navegador = webdriver.Chrome(chrome_options=options)
    navegador.get("https://internal.softlayer.com/Hardware/search/?data[Hardware][search][locationId]=983497&data[Hardware][search][hostname]=&data[Hardware][search][domain]=&data[Hardware][search][router]=&data[Hardware][search][hardwareStatusKeyName][]=HARDFAIL&data[Hardware][search][hardwareChassis][hardwareFunctionCode]=WEBSVR&data[Hardware][search][tags][tag][name]=&data[Hardware][search][tags][tag][internal]=0&data[Hardware][search][pooledServers]=all&data[Hardware][search][hardwarePoolId]=&data[Hardware][search][hardwarePoolStatus]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelId]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelCount]=0&data[Hardware][search][components][hardwareComponentModelId]=&data[Hardware][search][hardwareChassisId]=&data[Hardware][search][chassisSize]=&data[Hardware][search][softwareDescription]=&data[Hardware][search][id]=&data[Hardware][search][virtualHostId]=&data[Hardware][search][serialNumbers]=&data[Hardware][search][manufacturerSerialNumbers]=&data[Hardware][search][accountId]=&data[Hardware][search][hardwareChassis][scip]=&data[Hardware][search][components][hardwareComponentModel][scip]=&data[Hardware][search][address]=&data[Hardware][search][assetTag]=0&data[Hardware][search][internalNotes]=&data[Hardware][search][excludeRma]=&data[Hardware][search][noProcs]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelIds]=&data[Hardware][search][components][hardwareComponentModel][missingHardwareGenericComponentModelIds]=")
    sleep(4)
    user_name = navegador.find_element("id", "user_username")
    user_password = navegador.find_element("id", "user_password")
    user_token = navegador.find_element("id", "user_externaltoken")
    user_name.send_keys(usuario)
    user_password.send_keys(senha)
    user_token.send_keys(token)
    user_submit = navegador.find_element("id", "_index_form_submit")
    user_submit.submit()
    sleep(3)

    # capturar informacao da tela após autenticação - hardfail
    hardfail = navegador.find_element("id", "hardware_search_hardware_search_results__pagination_table_caption").text
    hardfail_final = hardfail.split()[3]
    sleep(2)

# active
    navegador.get(
        'https://internal.softlayer.com/Hardware/search/?data[Hardware][search][locationId]=983497&data[Hardware][search][hostname]=&data[Hardware][search][domain]=&data[Hardware][search][router]=&data[Hardware][search][hardwareStatusKeyName][]=ACTIVE&data[Hardware][search][hardwareChassis][hardwareFunctionCode]=WEBSVR&data[Hardware][search][tags][tag][name]=&data[Hardware][search][tags][tag][internal]=0&data[Hardware][search][pooledServers]=all&data[Hardware][search][hardwarePoolId]=&data[Hardware][search][hardwarePoolStatus]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelId]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelCount]=0&data[Hardware][search][components][hardwareComponentModelId]=&data[Hardware][search][hardwareChassisId]=&data[Hardware][search][chassisSize]=&data[Hardware][search][softwareDescription]=&data[Hardware][search][id]=&data[Hardware][search][virtualHostId]=&data[Hardware][search][serialNumbers]=&data[Hardware][search][manufacturerSerialNumbers]=&data[Hardware][search][accountId]=&data[Hardware][search][hardwareChassis][scip]=&data[Hardware][search][components][hardwareComponentModel][scip]=&data[Hardware][search][address]=&data[Hardware][search][assetTag]=0&data[Hardware][search][internalNotes]=&data[Hardware][search][excludeRma]=&data[Hardware][search][noProcs]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelIds]=&data[Hardware][search][components][hardwareComponentModel][missingHardwareGenericComponentModelIds]=')
    active = navegador.find_element("id", "hardware_search_hardware_search_results__pagination_table_caption").text
    active_final = active.split()[3]
    sleep(2)

# admin_hold
    navegador.get(
        'https://internal.softlayer.com/Hardware/search/?data[Hardware][search][locationId]=983497&data[Hardware][search][hostname]=&data[Hardware][search][domain]=&data[Hardware][search][router]=&data[Hardware][search][hardwareStatusKeyName][]=ADMIN_HOLD&data[Hardware][search][hardwareChassis][hardwareFunctionCode]=WEBSVR&data[Hardware][search][tags][tag][name]=&data[Hardware][search][tags][tag][internal]=0&data[Hardware][search][pooledServers]=all&data[Hardware][search][hardwarePoolId]=&data[Hardware][search][hardwarePoolStatus]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelId]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelCount]=0&data[Hardware][search][components][hardwareComponentModelId]=&data[Hardware][search][hardwareChassisId]=&data[Hardware][search][chassisSize]=&data[Hardware][search][softwareDescription]=&data[Hardware][search][id]=&data[Hardware][search][virtualHostId]=&data[Hardware][search][serialNumbers]=&data[Hardware][search][manufacturerSerialNumbers]=&data[Hardware][search][accountId]=&data[Hardware][search][hardwareChassis][scip]=&data[Hardware][search][components][hardwareComponentModel][scip]=&data[Hardware][search][address]=&data[Hardware][search][assetTag]=0&data[Hardware][search][internalNotes]=&data[Hardware][search][excludeRma]=&data[Hardware][search][noProcs]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelIds]=&data[Hardware][search][components][hardwareComponentModel][missingHardwareGenericComponentModelIds]=')
    admin_hold = navegador.find_element("id", "hardware_search_hardware_search_results__pagination_table_caption").text
    admin_hold_final = admin_hold.split()[3]
    sleep(2)

    # missing parts
    navegador.get(
        'https://internal.softlayer.com/Hardware/search/?data[Hardware][search][locationId]=983497&data[Hardware][search][hostname]=&data[Hardware][search][domain]=&data[Hardware][search][router]=&data[Hardware][search][hardwareStatusKeyName][]=MISSING_PARTS&data[Hardware][search][hardwareChassis][hardwareFunctionCode]=WEBSVR&data[Hardware][search][tags][tag][name]=&data[Hardware][search][tags][tag][internal]=0&data[Hardware][search][pooledServers]=all&data[Hardware][search][hardwarePoolId]=&data[Hardware][search][hardwarePoolStatus]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelId]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelCount]=0&data[Hardware][search][components][hardwareComponentModelId]=&data[Hardware][search][hardwareChassisId]=&data[Hardware][search][chassisSize]=&data[Hardware][search][softwareDescription]=&data[Hardware][search][id]=&data[Hardware][search][virtualHostId]=&data[Hardware][search][serialNumbers]=&data[Hardware][search][manufacturerSerialNumbers]=&data[Hardware][search][accountId]=&data[Hardware][search][hardwareChassis][scip]=&data[Hardware][search][components][hardwareComponentModel][scip]=&data[Hardware][search][address]=&data[Hardware][search][assetTag]=0&data[Hardware][search][internalNotes]=&data[Hardware][search][excludeRma]=&data[Hardware][search][noProcs]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelIds]=&data[Hardware][search][components][hardwareComponentModel][missingHardwareGenericComponentModelIds]=')
    missing = navegador.find_element("id", "hardware_search_hardware_search_results__pagination_table_caption").text
    missing_final = missing.split()[3]
    sleep(2)

    # deploy
    navegador.get(
        'https://internal.softlayer.com/Hardware/search/?data[Hardware][search][locationId]=983497&data[Hardware][search][hostname]=&data[Hardware][search][domain]=&data[Hardware][search][router]=&data[Hardware][search][hardwareStatusKeyName][]=DEPLOY&data[Hardware][search][hardwareChassis][hardwareFunctionCode]=WEBSVR&data[Hardware][search][tags][tag][name]=&data[Hardware][search][tags][tag][internal]=0&data[Hardware][search][pooledServers]=all&data[Hardware][search][hardwarePoolId]=&data[Hardware][search][hardwarePoolStatus]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelId]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelCount]=0&data[Hardware][search][components][hardwareComponentModelId]=&data[Hardware][search][hardwareChassisId]=&data[Hardware][search][chassisSize]=&data[Hardware][search][softwareDescription]=&data[Hardware][search][id]=&data[Hardware][search][virtualHostId]=&data[Hardware][search][serialNumbers]=&data[Hardware][search][manufacturerSerialNumbers]=&data[Hardware][search][accountId]=&data[Hardware][search][hardwareChassis][scip]=&data[Hardware][search][components][hardwareComponentModel][scip]=&data[Hardware][search][address]=&data[Hardware][search][assetTag]=0&data[Hardware][search][internalNotes]=&data[Hardware][search][excludeRma]=&data[Hardware][search][noProcs]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelIds]=&data[Hardware][search][components][hardwareComponentModel][missingHardwareGenericComponentModelIds]=')
    deploy = navegador.find_element("id", "hardware_search_hardware_search_results__pagination_table_caption").text
    deploy_final = deploy.split()[3]
    sleep(2)

    # deploy2
    navegador.get(
        'https://internal.softlayer.com/Hardware/search/?data[Hardware][search][locationId]=983497&data[Hardware][search][locationId_chooser]=&data[Hardware][search][hostname]=&data[Hardware][search][domain]=&data[Hardware][search][router]=&data[Hardware][search][hardwareStatusKeyName][]=DEPLOY2&data[Hardware][search][hardwareChassis][hardwareFunctionCode]=WEBSVR&data[Hardware][search][tags][tag][name]=&data[Hardware][search][tags][tag][internal]=0&data[Hardware][search][pooledServers]=all&data[Hardware][search][hardwarePoolId]=&data[Hardware][search][hardwarePoolStatus]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelId]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelCount]=0&data[Hardware][search][components][hardwareComponentModelId]=&data[Hardware][search][hardwareChassisId]=&data[Hardware][search][chassisSize]=&data[Hardware][search][softwareDescription]=&data[Hardware][search][id]=&data[Hardware][search][virtualHostId]=&data[Hardware][search][serialNumbers]=&data[Hardware][search][manufacturerSerialNumbers]=&data[Hardware][search][accountId]=&data[Hardware][search][hardwareChassis][scip]=&data[Hardware][search][components][hardwareComponentModel][scip]=&data[Hardware][search][address]=&data[Hardware][search][assetTag]=0&data[Hardware][search][internalNotes]=&data[Hardware][search][excludeRma]=&data[Hardware][search][noProcs]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelIds]=&data[Hardware][search][components][hardwareComponentModel][missingHardwareGenericComponentModelIds]=')
    deploy2 = navegador.find_element("id", "hardware_search_hardware_search_results__pagination_table_caption").text
    deploy2_final = deploy2.split()[3]
    sleep(2)

    # firmware_wait
    navegador.get(
        'https://internal.softlayer.com/Hardware/search/?data[Hardware][search][locationId]=983497&data[Hardware][search][hostname]=&data[Hardware][search][domain]=&data[Hardware][search][router]=&data[Hardware][search][hardwareStatusKeyName][]=FIRMWARE_WAIT&data[Hardware][search][hardwareChassis][hardwareFunctionCode]=WEBSVR&data[Hardware][search][tags][tag][name]=&data[Hardware][search][tags][tag][internal]=0&data[Hardware][search][pooledServers]=all&data[Hardware][search][hardwarePoolId]=&data[Hardware][search][hardwarePoolStatus]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelId]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelCount]=0&data[Hardware][search][components][hardwareComponentModelId]=&data[Hardware][search][hardwareChassisId]=&data[Hardware][search][chassisSize]=&data[Hardware][search][softwareDescription]=&data[Hardware][search][id]=&data[Hardware][search][virtualHostId]=&data[Hardware][search][serialNumbers]=&data[Hardware][search][manufacturerSerialNumbers]=&data[Hardware][search][accountId]=&data[Hardware][search][hardwareChassis][scip]=&data[Hardware][search][components][hardwareComponentModel][scip]=&data[Hardware][search][address]=&data[Hardware][search][assetTag]=0&data[Hardware][search][internalNotes]=&data[Hardware][search][excludeRma]=&data[Hardware][search][noProcs]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelIds]=&data[Hardware][search][components][hardwareComponentModel][missingHardwareGenericComponentModelIds]=')
    firmware = navegador.find_element("id", "hardware_search_hardware_search_results__pagination_table_caption").text
    firmware_final = firmware.split()[3]
    sleep(2)

    # inventory
    navegador.get(
        'https://internal.softlayer.com/Hardware/search/?data[Hardware][search][locationId]=983497&data[Hardware][search][hostname]=&data[Hardware][search][domain]=&data[Hardware][search][router]=&data[Hardware][search][hardwareStatusKeyName][]=INVENTORY&data[Hardware][search][hardwareChassis][hardwareFunctionCode]=WEBSVR&data[Hardware][search][tags][tag][name]=&data[Hardware][search][tags][tag][internal]=0&data[Hardware][search][pooledServers]=all&data[Hardware][search][hardwarePoolId]=&data[Hardware][search][hardwarePoolStatus]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelId]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelCount]=0&data[Hardware][search][components][hardwareComponentModelId]=&data[Hardware][search][hardwareChassisId]=&data[Hardware][search][chassisSize]=&data[Hardware][search][softwareDescription]=&data[Hardware][search][id]=&data[Hardware][search][virtualHostId]=&data[Hardware][search][serialNumbers]=&data[Hardware][search][manufacturerSerialNumbers]=&data[Hardware][search][accountId]=&data[Hardware][search][hardwareChassis][scip]=&data[Hardware][search][components][hardwareComponentModel][scip]=&data[Hardware][search][address]=&data[Hardware][search][assetTag]=0&data[Hardware][search][internalNotes]=&data[Hardware][search][excludeRma]=&data[Hardware][search][noProcs]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelIds]=&data[Hardware][search][components][hardwareComponentModel][missingHardwareGenericComponentModelIds]=')
    inventory = navegador.find_element("id", "hardware_search_hardware_search_results__pagination_table_caption").text
    inventory_final = inventory.split()[3]
    sleep(2)

    # liquidation
    navegador.get(
        'https://internal.softlayer.com/Hardware/search/?data[Hardware][search][locationId]=983497&data[Hardware][search][hostname]=&data[Hardware][search][domain]=&data[Hardware][search][router]=&data[Hardware][search][hardwareStatusKeyName][]=LIQUIDATION&data[Hardware][search][hardwareChassis][hardwareFunctionCode]=WEBSVR&data[Hardware][search][tags][tag][name]=&data[Hardware][search][tags][tag][internal]=0&data[Hardware][search][pooledServers]=all&data[Hardware][search][hardwarePoolId]=&data[Hardware][search][hardwarePoolStatus]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelId]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelCount]=0&data[Hardware][search][components][hardwareComponentModelId]=&data[Hardware][search][hardwareChassisId]=&data[Hardware][search][chassisSize]=&data[Hardware][search][softwareDescription]=&data[Hardware][search][id]=&data[Hardware][search][virtualHostId]=&data[Hardware][search][serialNumbers]=&data[Hardware][search][manufacturerSerialNumbers]=&data[Hardware][search][accountId]=&data[Hardware][search][hardwareChassis][scip]=&data[Hardware][search][components][hardwareComponentModel][scip]=&data[Hardware][search][address]=&data[Hardware][search][assetTag]=0&data[Hardware][search][internalNotes]=&data[Hardware][search][excludeRma]=&data[Hardware][search][noProcs]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelIds]=&data[Hardware][search][components][hardwareComponentModel][missingHardwareGenericComponentModelIds]=')
    liquidation = navegador.find_element("id", "hardware_search_hardware_search_results__pagination_table_caption").text
    liquidation_final = liquidation.split()[3]
    sleep(2)

    # macwait
    navegador.get(
        'https://internal.softlayer.com/Hardware/search/?data[Hardware][search][locationId]=983497&data[Hardware][search][locationId_chooser]=&data[Hardware][search][hostname]=&data[Hardware][search][domain]=&data[Hardware][search][router]=&data[Hardware][search][hardwareStatusKeyName][]=MACWAIT&data[Hardware][search][hardwareChassis][hardwareFunctionCode]=WEBSVR&data[Hardware][search][tags][tag][name]=&data[Hardware][search][tags][tag][internal]=0&data[Hardware][search][pooledServers]=all&data[Hardware][search][hardwarePoolId]=&data[Hardware][search][hardwarePoolStatus]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelId]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelCount]=0&data[Hardware][search][components][hardwareComponentModelId]=&data[Hardware][search][hardwareChassisId]=&data[Hardware][search][chassisSize]=&data[Hardware][search][softwareDescription]=&data[Hardware][search][id]=&data[Hardware][search][virtualHostId]=&data[Hardware][search][serialNumbers]=&data[Hardware][search][manufacturerSerialNumbers]=&data[Hardware][search][accountId]=&data[Hardware][search][hardwareChassis][scip]=&data[Hardware][search][components][hardwareComponentModel][scip]=&data[Hardware][search][address]=&data[Hardware][search][assetTag]=0&data[Hardware][search][internalNotes]=&data[Hardware][search][excludeRma]=&data[Hardware][search][noProcs]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelIds]=&data[Hardware][search][components][hardwareComponentModel][missingHardwareGenericComponentModelIds]=')
    macwait = navegador.find_element("id", "hardware_search_hardware_search_results__pagination_table_caption").text
    macwait_final = macwait.split()[3]
    sleep(2)

    # planned
    navegador.get(
        'https://internal.softlayer.com/Hardware/search/?data[Hardware][search][locationId]=983497&data[Hardware][search][hostname]=&data[Hardware][search][domain]=&data[Hardware][search][router]=&data[Hardware][search][hardwareStatusKeyName][]=PLANNED&data[Hardware][search][hardwareChassis][hardwareFunctionCode]=WEBSVR&data[Hardware][search][tags][tag][name]=&data[Hardware][search][tags][tag][internal]=0&data[Hardware][search][pooledServers]=all&data[Hardware][search][hardwarePoolId]=&data[Hardware][search][hardwarePoolStatus]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelId]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelCount]=0&data[Hardware][search][components][hardwareComponentModelId]=&data[Hardware][search][hardwareChassisId]=&data[Hardware][search][chassisSize]=&data[Hardware][search][softwareDescription]=&data[Hardware][search][id]=&data[Hardware][search][virtualHostId]=&data[Hardware][search][serialNumbers]=&data[Hardware][search][manufacturerSerialNumbers]=&data[Hardware][search][accountId]=&data[Hardware][search][hardwareChassis][scip]=&data[Hardware][search][components][hardwareComponentModel][scip]=&data[Hardware][search][address]=&data[Hardware][search][assetTag]=0&data[Hardware][search][internalNotes]=&data[Hardware][search][excludeRma]=&data[Hardware][search][noProcs]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelIds]=&data[Hardware][search][components][hardwareComponentModel][missingHardwareGenericComponentModelIds]=')
    planned = navegador.find_element("id", "hardware_search_hardware_search_results__pagination_table_caption").text
    planned_final = planned.split()[3]
    sleep(2)

    # reclaim
    navegador.get(
        'https://internal.softlayer.com/Hardware/search/?data[Hardware][search][locationId]=983497&data[Hardware][search][hostname]=&data[Hardware][search][domain]=&data[Hardware][search][router]=&data[Hardware][search][hardwareStatusKeyName][]=RECLAIM&data[Hardware][search][hardwareChassis][hardwareFunctionCode]=WEBSVR&data[Hardware][search][tags][tag][name]=&data[Hardware][search][tags][tag][internal]=0&data[Hardware][search][pooledServers]=all&data[Hardware][search][hardwarePoolId]=&data[Hardware][search][hardwarePoolStatus]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelId]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelCount]=0&data[Hardware][search][components][hardwareComponentModelId]=&data[Hardware][search][hardwareChassisId]=&data[Hardware][search][chassisSize]=&data[Hardware][search][softwareDescription]=&data[Hardware][search][id]=&data[Hardware][search][virtualHostId]=&data[Hardware][search][serialNumbers]=&data[Hardware][search][manufacturerSerialNumbers]=&data[Hardware][search][accountId]=&data[Hardware][search][hardwareChassis][scip]=&data[Hardware][search][components][hardwareComponentModel][scip]=&data[Hardware][search][address]=&data[Hardware][search][assetTag]=0&data[Hardware][search][internalNotes]=&data[Hardware][search][excludeRma]=&data[Hardware][search][noProcs]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelIds]=&data[Hardware][search][components][hardwareComponentModel][missingHardwareGenericComponentModelIds]=')
    reclaim = navegador.find_element("id", "hardware_search_hardware_search_results__pagination_table_caption").text
    reclaim_final = reclaim.split()[3]
    sleep(2)

    # reserved
    navegador.get(
        'https://internal.softlayer.com/Hardware/search/?data[Hardware][search][locationId]=983497&data[Hardware][search][hostname]=&data[Hardware][search][domain]=&data[Hardware][search][router]=&data[Hardware][search][hardwareStatusKeyName][]=RESERVED&data[Hardware][search][hardwareChassis][hardwareFunctionCode]=WEBSVR&data[Hardware][search][tags][tag][name]=&data[Hardware][search][tags][tag][internal]=0&data[Hardware][search][pooledServers]=all&data[Hardware][search][hardwarePoolId]=&data[Hardware][search][hardwarePoolStatus]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelId]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelCount]=0&data[Hardware][search][components][hardwareComponentModelId]=&data[Hardware][search][hardwareChassisId]=&data[Hardware][search][chassisSize]=&data[Hardware][search][softwareDescription]=&data[Hardware][search][id]=&data[Hardware][search][virtualHostId]=&data[Hardware][search][serialNumbers]=&data[Hardware][search][manufacturerSerialNumbers]=&data[Hardware][search][accountId]=&data[Hardware][search][hardwareChassis][scip]=&data[Hardware][search][components][hardwareComponentModel][scip]=&data[Hardware][search][address]=&data[Hardware][search][assetTag]=0&data[Hardware][search][internalNotes]=&data[Hardware][search][excludeRma]=&data[Hardware][search][noProcs]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelIds]=&data[Hardware][search][components][hardwareComponentModel][missingHardwareGenericComponentModelIds]=')
    reserved = navegador.find_element("id", "hardware_search_hardware_search_results__pagination_table_caption").text
    reserved_final = reserved.split()[3]
    sleep(2)

    # spare
    navegador.get(
        'https://internal.softlayer.com/Hardware/search/?data[Hardware][search][locationId]=983497&data[Hardware][search][hostname]=&data[Hardware][search][domain]=&data[Hardware][search][router]=&data[Hardware][search][hardwareStatusKeyName][]=SPARE&data[Hardware][search][hardwareChassis][hardwareFunctionCode]=WEBSVR&data[Hardware][search][tags][tag][name]=&data[Hardware][search][tags][tag][internal]=0&data[Hardware][search][pooledServers]=all&data[Hardware][search][hardwarePoolId]=&data[Hardware][search][hardwarePoolStatus]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelId]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelCount]=0&data[Hardware][search][components][hardwareComponentModelId]=&data[Hardware][search][hardwareChassisId]=&data[Hardware][search][chassisSize]=&data[Hardware][search][softwareDescription]=&data[Hardware][search][id]=&data[Hardware][search][virtualHostId]=&data[Hardware][search][serialNumbers]=&data[Hardware][search][manufacturerSerialNumbers]=&data[Hardware][search][accountId]=&data[Hardware][search][hardwareChassis][scip]=&data[Hardware][search][components][hardwareComponentModel][scip]=&data[Hardware][search][address]=&data[Hardware][search][assetTag]=0&data[Hardware][search][internalNotes]=&data[Hardware][search][excludeRma]=&data[Hardware][search][noProcs]=&data[Hardware][search][components][hardwareComponentModel][hardwareGenericComponentModelIds]=&data[Hardware][search][components][hardwareComponentModel][missingHardwareGenericComponentModelIds]=')
    spare = navegador.find_element("id", "hardware_search_hardware_search_results__pagination_table_caption").text
    spare_final = spare.split()[3]
    sleep(2)

    # salvar no txt
    with open('results.txt', 'w') as arquivo:
        arquivo.write(f"Active: {active_final} \n")
        arquivo.write(f"Deploy: {deploy_final} \n")
        arquivo.write(f"Deploy2: {deploy2_final} \n")
        arquivo.write(f"Firmware_Wait: {firmware_final} \n")
        arquivo.write(f"Hardfail: {hardfail_final} \n")
        arquivo.write(f"Inventory: {inventory_final} \n")
        arquivo.write(f"Liquidation: {liquidation_final} \n")
        arquivo.write(f"Macwait: {macwait_final} \n")
        arquivo.write(f"Missing: {missing_final} \n")
        arquivo.write(f"Planned: {planned_final} \n")
        arquivo.write(f"Reclaim: {reclaim_final} \n")
        arquivo.write(f"Reserved: {reserved_final} \n")
        arquivo.write(f"Spare: {spare_final} \n\n")
        arquivo.close()
        #COMEÇA AGORA O TICKET AUDIT

    navegador.get("https://internal.softlayer.com/Ticket/advancedTicketSearch/?data[Tickets][searchFilter][accountId]=&data[Tickets][searchFilter][ticketId]=&data[Tickets][searchFilter][employeeId]=&data[Tickets][searchFilter][companyName]=&data[Tickets][searchFilter][title]=&data[Tickets][searchFilter][groupId]=1010&data[Tickets][searchFilter][user]=&data[Tickets][searchFilter][searchStatus]=active&data[Tickets][searchFilter][internalGroupId]=&data[Tickets][searchFilter][hardwareId]=&data[Tickets][searchFilter][virtualGuestId]=&data[Tickets][searchFilter][serverAdmin]=&data[Tickets][searchFilter][datacenter]=983497&data[Tickets][searchFilter][brandId]=&data[Tickets][searchFilter][escalationStatus]=&data[Tickets][searchFilter][createDate][start]=&data[Tickets][searchFilter][createDate][end]=&data[Tickets][searchFilter][supportClassification]=ALL&data[Tickets][searchFilter][modifyDate][type]=&data[Tickets][searchFilter][modifyDate][dateThreshold]=&data[Tickets][searchFilter][priorityLevel]=")
    #Criar lista de horarios shifts
    tickets = []
    tickets_dois = []
    today = datetime.today().strftime('%Y-%m-%d')
    evening_schedule = ["15","16","17","18","19","20","21","22","23"]
    day_schedule = ["8","9","10","11","12","13","14","15"]
    overnight_schedule = ["0","1","2","3","4","5","6","7"]

    #abrir link página e criar lista de tickets em preview
    for i in navegador.find_elements(By.LINK_TEXT, "[Preview]"):
        teste = i.get_attribute("href")
        tickets.append(teste)

    print(tickets)

    #Pegar lista em preview e converter para Edit
    for l in tickets:
        variavel = l.replace("Preview","Edit")
        tickets_dois.append(variavel)

# Looping para tratar cada ticket
    for batata in tickets_dois:
        navegador.get(batata)

# Pega informação do Re-yellow
        url = navegador.find_element(By.ID, "cancelYellowShowDate").text
        get_url = navegador.current_url

        #Pega titulo do ticket
        ticket_title = navegador.find_element(By.ID, "ticket_title")
        ticket_title_final = ticket_title.get_attribute('value')

        #Verificar se o re-yellow está vazio, caso sim, AUTO CLOSE
        if url == "":
            print("Auto-Close")

        else:

            # Pega horario
            new_hour = url.split()[1]

            # Converte horario para GMT-6 adicionando +3 horas (transforma em inteiro para fazer isso
            if int(new_hour[0:2]) + 3 == 24:
                new_hour_1 = 0
            elif int(new_hour[0:2]) + 3 == 25:
                new_hour_1 = 1
            elif int(new_hour[0:2]) + 3 == 26:
                new_hour_1 = 2
            else:
                new_hour_1 = int(new_hour[0:2]) + 3

            # Pega horario inteiro novamente, com as modificações
            new_hour_final = str(new_hour_1) + new_hour[2:5]

            # Converte INT da hora em string novamente para procurar na lista
            new_hour_string = str(new_hour_1)

            #Converte o mes para numero
            url_1 = str(url.split()[0])

            if url_1[5:8] == "Jan":
                new_url = url_1.replace("Jan","01")
            elif url_1[5:8] == "Feb":
                new_url = url_1.replace("Feb","02")
            elif url_1[5:8] == "Mar":
                new_url = url_1.replace("Mar", "03")
            elif url_1[5:8] == "Apr":
                new_url = url_1.replace("Apr", "04")
            elif url_1[5:8] == "May":
                new_url = url_1.replace("May","05")
            elif url_1[5:8] == "Jun":
                new_url = url_1.replace("Jun","06")
            elif url_1[5:8] == "Jul":
                new_url = url_1.replace("Jul", "07")
            elif url_1[5:8] == "Aug":
                new_url = url_1.replace("Aug", "08")
            elif url_1[5:8] == "Sep":
                new_url = url_1.replace("Sep","09")
            elif url_1[5:8] == "Oct":
                new_url = url_1.replace("Oct","10")
            elif url_1[5:8] == "Nov":
                new_url = url_1.replace("Nov", "11")
            elif url_1[5:8] == "Dec":
                new_url = url_1.replace("Dec", "12")




            #Faz check se o ticket vai cair no dia e qual shift está selecionado
            if new_url == today and evening_schedule.count(new_hour_string) > 0 and shift == "Evening Shift":
                with open('results.txt', 'a') as arquivo:
                    arquivo.write(f"{ticket_title_final} - {get_url} - {new_url} - {new_hour_final}\n")
            elif new_url == today and day_schedule.count(new_hour_string) > 0 and shift == "Day Shift":
                with open('results.txt', 'a') as arquivo:
                    arquivo.write(f"{ticket_title_final} - {get_url} - {new_url} - {new_hour_final}\n")
            elif new_url == today and overnight_schedule.count(new_hour_string) > 0 and shift == "Overnight Shift":
                with open('results.txt', 'a') as arquivo:
                    arquivo.write(f"{ticket_title_final} - {get_url} - {new_url} - {new_hour_final}\n")

    messagebox.showinfo("showinfo", "Check Results.txt")







# método principal
def login():
    global janela_login
    global txt_usuario
    global txt_senha
    global txt_token
    global variable


# vamos criar a tela de login
    janela_login = Tk()

    shifts = ["Day Shift", "Evening Shift", "Overnight Shift"]

    variable = StringVar(janela_login)
    variable.set(shifts[0])  # default value


# vamos definir o tamanho da janela
    janela_login.geometry("260x200")

    # o titulo da janela
    janela_login.title("LOGIN")

    # evitamos que a janela seja redimensionada
    janela_login.resizable(False, False)

    # vamos configurar o grid
    janela_login.columnconfigure(1, weight=1)
    janela_login.columnconfigure(1, weight=3)
    janela_login.columnconfigure(1, weight=3)

    # nome do usuário
    label_usuario = Label(janela_login, text="Usuário:")
    label_usuario.grid(column=0, row=0, sticky=W, padx=15, pady=10)
    txt_usuario = Entry(janela_login, width=28)
    txt_usuario.grid(column=1, row=0, sticky=E, padx=15, pady=8)

    # senha
    label_senha = Label(janela_login, text="Senha:")
    label_senha.grid(column=0, row=1, sticky=W, padx=15, pady=0)
    txt_senha = Entry(janela_login, show="*", width=28)
    txt_senha.grid(column=1, row=1, sticky=E, padx=15, pady=10)

    # token
    label_token = Label(janela_login, text="Token:")
    label_token.grid(column=0, row=2, sticky=W, padx=15, pady=10)
    txt_token = Entry(janela_login, show="*", width=15)
    txt_token.grid(column=1, row=2, sticky=W, padx=15, pady=0)

    # token
    w = OptionMenu(janela_login, variable, *shifts)
    w.grid(column=1, row=3, sticky=E, padx=15, pady=10)

    # botão de login
    btn_login = Button(janela_login, text="Entrar", command=autenticar_usuario)
    btn_login.grid(column=1, row=4, sticky=E, padx=15, pady=10)

    # entramos no loop de eventos
    janela_login.mainloop()


login()
