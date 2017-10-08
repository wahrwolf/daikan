# daikan
information provider and action manager for spacecrafts based on REST API using flask

# WHAT?
Yes this is an aproach to create a framework that provide everything you need to control a spacecraft.

This project does not aim to acutal provide ready to rollout microcontroller friendly code to fly to the moon.
Its more about building a solid controller framework which can be easier managed and integrated.

Every main system (LSS, ACS, CDH, NAV, COM, EPS, HES) has a set of generic API actions.
Each systems has one or mutliple controller which provides those actions.
The CDH provides the routing and management of those controllers.

A spacecraft (or any other controllable system, like an arduionowired house) implements those actions thru devices which are controlled by an controller.

This allows to build userinterfaces and scripts for controlling an environmet thru capsulation.
It should be flexible enough to adapt new alien (maybe even extraterestial) devices into an existing system, while beiing solid and controllable.

The whole idea is based around the fact, that I want spacecraft debugging to be made as simple as possible.
An REST API approach has a few benefits:
 * easy user management
 * scalable
 * solid
 * integratable
 
 #TODO
 following controller still needs to be written:
 * Life Support (LSS)
 ** atmosphere
 ** water
 ** fod
 ** microbe
 * Attidude Control (ACS)
 ** stabilization
 ** articulation
 ** geometry
 ** actuators
 * Navigation (NAV)
 ** course
 ** tracking
 ** collission detection
 * bus system (CDH)
 ** logging
 ** user managment
 ** data pool
 * communicatin (COM)
 ** senders
 ** recievers/scanners
 * energy and power (EPS)
 ** generators
 ** batteries
 ** distribution
 * hazard and environment (HES)
 ** hull
 ** radiation
 ** temperature
 
 so we are working on it, but its a long way ;)
 
 # WHY?
 They are mutliple reasons:
 * there is no fancy spacecraft framework (PLS CORRECT ME IF I AM WRONG!!!)
 * we wanted to do some scifi LARP stuff and needed a platform
 * i wanted some shiny internet of things framework
 * did I mention spacecrafts?
 
 
 
 # Why Python/flask?
 I like both <3
