COMMENT_80 = "Only required to initiate TLS communication; all other communications use port 443"
COMMENT_443 = ""

ports = {
    '':  
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'ActionGroup':  
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'ApplicationInsightsAvailability':
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'AzureAD': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'AzureAdvancedThreatProtection': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'AzureApiManagement': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'AzureAppConfiguration': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'AzureAppService': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'AzureAppServiceManagement': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'AzureAutomation': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'AzureBackup': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'AzureBotService': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'AzureCognitiveSearch': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'AzureConnectors': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'AzureContainerRegistry': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'AzureCosmosDB': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'AzureDatabricks': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'AzureDataExplorerManagement': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'AzureEventGrid': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'AzureEventHub': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'AzureIdentity': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'AzureInformationProtection': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'AzureIoTHub': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'AzureKeyVault': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'AzureMachineLearning': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'AzureMonitor': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'AzurePortal': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'AzureResourceManager': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'AzureServiceBus': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'AzureSignalR': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'AzureSiteRecovery': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'AzureSQL': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'AzureStorage': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'AzureTrafficManager': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'BatchNodeManagement': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'CognitiveServicesManagement': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'DataFactory': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'ElasticAFD': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'GatewayManager': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'HDInsight': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'LogicApps': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'MicrosoftCloudAppSecurity': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'MicrosoftContainerRegistry': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'PowerBI': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'PowerQueryOnline': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'ServiceFabric': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'SqlManagement': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'StorageSyncService': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    'WindowsVirtualDesktop': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],

    ## Azure Public Cloud Only Services
    'AzureDataLake': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],
    
    'AzureDevSpaces': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],

    'AzureOpenDatasets': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],

    'Dynamics365ForMarketingEmail': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}],

    'AzureFrontDoor': 
                    [{'port': '80', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_80},
                    {'port': '443', 'protocol': 'TCP (6)', 'io':'both' , 'classification':'U' , 'comment': COMMENT_443}]
    }

