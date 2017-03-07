import sys
from TestCase import TestCase
from kinetic_application_runner import kinetic_application_runner
from kinetic_controller import kinetic_controller
class KineticTestCase(TestCase):

    def __init__(self, configFilePath):
        TestCase.controllerName = "kinetic"
        TestCase.mainConfigFile = configFilePath


    def stopApplication(self):
        print "stopping application"
	self.apprunner.stopApp()


    def startController(self):
        print "running controller"
        self.kineticcontroller =  kinetic_controller()
        self.kineticcontroller.runController(self.dictionary)


    def startApplication(self, applicationName):
        print "running application"
        self.apprunner = kinetic_application_runner(self.dictionary, TestCase.testBedHomePath)
        #self.apprunner.setCodeDir("/src/main/java")
        #self.apprunner.setConfigFile("/home/vagrant/python/Master---Thesis/apps/floodlight/floodlightdefault.properties")
        #self.apprunner.setModuleFile("CHANGE")
        #self.apprunner.setTestBedModuleFile("CHANGE")
        #print self.dictionary
	#print TestCase.testBedHomePath
	self.apprunner.runApp(applicationName, self.dictionary, TestCase.testBedHomePath)


    def stopController(self):
        print "stopping controller"
        self.kineticcontroller.stopController()

    def setTestBedHome(self, testBedHomePath='/home/vagrant/python/Master---Thesis/'):
        TestCase.testBedHomePath = testBedHomePath

    def additionalConfigFile(self, configFilePath=None, configFileName = None):
        if configFilePath==None or configFileName == None:
            raise Exception('Please provide file path and name')
        else:
            print "reading additional config file"
            TestCase.configFiles[configFileName] = configFilePath