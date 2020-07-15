2020-02-20 (2.36.0)
-------------------

* MojeID
  * add new method for validated data update (no mojeid verification states canceling)
  * fix exception in send_new_pin3 method

2019-11-20 (2.35.1)
-------------------

* Update spec file for F31 and Centos/RHEL 8

2019-04-26 (2.35.0)
-------------------

* accounting interface
   * add optional custom tax date to import payment method (when specifying registrar manually)

2019-03-18 (2.34.0)
-------------------

* License GNU GPLv3+
* CMake fixes
* Autotools removal

2018-08-16 (2.33.0)
-------------------

* modify epp interface to support disclose flags policy configration
* mojeid
   * join fist/last name to name
* new interface for accounting (removed bank payements interfaces and structures)
* public request
   * status enum renaming
   * new verification type for requests (government)
* dropping unused structures

2018-04-20 (2.32.0)
-------------------

* add personal info into public request interface
* modify epp interface to support update contact poll message

2018-03-14 (2.31.0)
-------------------

* switch to new common date/time and buffer data types

2018-03-08 (2.30.0)
-------------------

* add renderMail method to mailer interface
* fix record statement interface (status deleteCandidate)

2017-12-20 (2.29.0)
-------------------

* statically compiled IDL for python

2017-09-12 (2.28.0)
-------------------

* epp interface contact method changed to support mailing address

2017-06-09 (2.27.0)
-------------------

* add interface for automatic keyset management

2017-03-13 (2.26.0)
-------------------

* dedicated interface for public requests (authinfo, object block/unblock requests)

2016-11-22 (2.25.1)
-------------------

* daphne idl fix
   * import new idl (Notification.idl) in ccReg.idl

2016-09-07 (2.25.0)
-------------------

* mojeid
   * method for direct contact validation
* new interface method for custom e-mail notification about domain going outzone (after expiration)

2016-04-08 (2.24.0)
-------------------

* mojeid interface reworked

2016-01-20 (2.23.0)
-------------------

* new whois and rdap backend interface refactoring and add methods used by webwhois client
* domainbrowser
   * interface documentation

2015-05-19 Jiri Sadek, Jan Korous, Jan Zima, Michal Strnad (2.22.0)
-------------------------------------------------------------------

* domainbrowser
   * interface reworked
   * add flag to change user preference whether send domain warning letter or not
   * add mailing address to signed-on user contact info
* mojeid
   * new method for (re)send mojeid card
   * message limit exception
* adifd
   * add destination account number to payment detail

2015-03-01 Michal Strnad (2.21.0)
---------------------------------

* mojeid
   * add method for new pin3 resending

2015-02-09 Jan Zima (2.20.2)
----------------------------

* mojeid
   * add contact linked status info to output structure of status synchronization method

2014-12-12 Jiri Sadek, Jan Korous, Jan Zima, Michal Strnad (2.20.1)
-------------------------------------------------------------------

* mojeid
   * fix interface for verification state synchronization
   * removed unused ssn_type attribute from contact struct

2014-10-17 Jiri Sadek, Michal Strnad (2.20.0)
---------------------------------------------

* mojeid
   * add 'company_name' to address struct
   * request type for re-identification
   * interface for retrieving contact state and states changes reworked
* adifd
   * add additional contact addreses to detail struct

2014-10-02 Jiri Sadek (2.19.1)
------------------------------

* fix
   * new adifd interface exception (message resend)

2014-08-01 Jan Korous, Jan Zima (2.19.0)
----------------------------------------

* new idl for whois prototype (now used for rdap)
* domain browser interface
   * minor fixes
   * add merge contacts feature

2014-06-12 Jan Korous (2.18.0)
------------------------------

* new interface for admin. contact verification
* separation of common date time and nullable types

2014-02-13 Michal Strnad (2.17.0)
---------------------------------

* adifd
   * methods for pin2 and pin3 resending (for given public request)

2013-11-11 Michal Strnad, Jan Zima (2.16.0)
-------------------------------------------

* new interface for administrative blocking/unblocking domains (and holders)
* fix epp poll req/ack commands
   * overflow of count values

2013-08-07 Zdeněk Böhm, Jiri Sadek (2.15.0)
-------------------------------------------

* mojeid
   * managing of disclose flags removed from interface
* domain browser
   * add new interface

2013-06-05 Jiri Sadek (2.14.1)
------------------------------

* mojeid
   * getUnregistrableHandlesIter() method - returns iterable object to transfer contact handles to client by 
     small chunks (should be a replacement for slow getUnregistrableHandles())

2013-04-02 Jiri Sadek (2.14.0)
------------------------------

* epp
   * interface changes for update object poll messages

2012-11-21 Jan Zima (2.13.0)
----------------------------

* mojeid
   * contactUnidentifyPrepare(..) method removed

2012-09-05 Jiri Sadek, Juraj Vicenik, Jan Zima (2.12.0)
-------------------------------------------------------

* added contact verification interface
* mojeid
   * new method for account cancellation
* logger
   * removed output flag from properties interface (it is now set implicitly by create/close request methods)
* adifd
   * method for getting summary of expiring domains

2012-05-11 Jiri Sadek, Juraj Vicenik, Jan Zima (2.11.0)
-------------------------------------------------------

* mojeid
   * method returning list of unregistrable contact handles
   * contact authinfo getter

2012-04-27 Jiri Sadek, Juraj Vicenik, Jan Zima (2.10.0)
-------------------------------------------------------

* epp action removed from fred

2011-12-23 Jiri Sadek (2.9.1)
-----------------------------

* adifd
   * history record switched from action_id to logger request_id

2011-10-17 Jiri Sadek, Juraj Vicenik, Jan Zima (2.9.0)
------------------------------------------------------

* admin
   * registrar blocking interface
   * removed invoice_id from payment/statement filters
   * invoice detail struct changed data type for vatrate attribute to string
* epp
   * credit_info structure changed credit amount data type to string

2011-09-26 Jiri Sadek, Juraj Vicenik (2.8.2)
--------------------------------------------

* epp - interface for deleting all active sessions for given registrar
* adifd/epp - interface to get last request fee info

2011-08-11 Juraj Vicenik (2.8.1)
--------------------------------

* logger - request count method by username

2011-07-04 Jiri Sadek, Juraj Vicenik (2.8.0)
--------------------------------------------

* new poll message - request fee info
* logger - simple request count method

2011-05-26 Jiri Sadek (2.7.1)
-----------------------------

* mojeid - identification string output param for contactCreate/Transfer (2-PC)

2011-05-20 Juraj Vicenik (2.7.0)
--------------------------------

* mojeid
   * 2-PC for contactCreate
   * 2-PC for contactTransfer

2011-02-24 Jan Zima, Tomas Divis, Juraj Vicenik (2.6.0)
-------------------------------------------------------

* authinfo to MojeID contact struct
* datatype for request id changed to unsigned long long
* separate interface for Admin and Whois
* idl dependencies simplified
* removed "underscored" (grouping) idls for specific usage
* removed unused code

2010-11-22 Jiri Sadek (2.5.3)
-----------------------------

* New exceptions in MojeID interface
   * processIdentification, createValidationRequest

* fred-adifd new filters (contact, messages)

2010-10-18 Jiri Sadek, Juraj Vicenik, Jan Zima (2.5.1)
------------------------------------------------------

* Changes in MojeID interface

2010-09-29 Jiri Sadek, Juraj Vicenik, Jan Zima (2.5.0)
------------------------------------------------------

* Logger interface refactoring
* Messages interface added
* MojeID interface added
* PageTable now support offset, limit and timeout

2010-07-22 Juraj Vicenik (2.4.1)
--------------------------------

* Request detail structure updated (user_name)

2010-06-17 Jiri Sadek (2.4.0)
-----------------------------

* Unused interfaces removed
* Registrar groups interface
* Registrar certification interface
* Logger - method for getting services
* EPP - interface preparation for mandatory logger usage (requestid passing)

2010-03-09 Jiri Sadek, Juraj Vicenik (2.3.2)
--------------------------------------------

* Method for changing bank payment type method added to banking interface
* Logger - Admin filtering interface separated (moved from Admin to Logger)

2010-02-24 Jan Zima (2.3.1)
---------------------------

* Interface method for signed domains count

2010-02-16 Juraj Vicenik, Jan Zima, Jiri Sadek (2.3.0)
------------------------------------------------------

* Interface for audit (Logger) component
* Interface for banking module
* Registar and Zone access inteface refactoring

2009-11-09 Jiri Sadek, Juraj Vicenik (2.2.0)
--------------------------------------------

* Interface for enum dictionary project
* Fixed public requests interface

2009-06-30 Ales Dolezal (2.1.1)
-------------------------------

* New function which allow manually add domain into the zone.

2008-10-18 Jiri Sadek, Ales Dolezal (2.1.0)
-------------------------------------------

* Adding DNSKEY record to all API
	* new DNSKey_str structure created
	* added to KeySetDetail, KeySet and KeySet::Detail structures
	* added to KeysetCreate and KeySetUpdate EPP interface methods
	* added to ParamError list

2008-09-18 Jiri Sadek
---------------------

* release 2.0.1
* Refactoring
   * Invoicing naming changes
   * Public request details type change
   * Mail detail attribute name and type change                
* Object states
   * Filter added
   * History of states into object details
* EPP action update
   * xml output
   * fixing response OK/Failed filter
   * adding new filter for response code

2008-08-15 Jiri Sadek, Ales Dolezal, Jaromir Talir
--------------------------------------------------

* release 2.0.0
* DNSSEC implementation, keyset object handled by all interfaces (EPP, Whois and Administration)
* History of changes in objects handled in administration interface
* Administration interface support enhanced inter object linkage driven by id of objects
* First version of new interface _Registry.idl that will replace old _Admin.idl

2008-07-13 Jiri Sadek
---------------------

* release 1.11.0
* Added method numRowsOverLimit() to PageTable to detect if number of rows in result set was limited by defined constant
* Updated EppAction 
   * filter for Requested Handle -> object doesn't need to be in registry
   * output xml added to detail
* EppActionType changed from string only to id - name pair for proper filtering
* getSortedBy() method rewritten in order to getting sort column and also sort direction
	
2008-06-24 Jiri Sadek
---------------------

* release 1.10.0
* New domain filters added (outzone date, cancel date)
* New Mail, File and Invoice filters added
* Filter Iterator::getFilter method throwing exception 
* Added destroySession(session_id) method for Admin object
* Some Id filters exposed to CORBA due to ticket #1520

2008-05-30 Jaromir Talir <jaromir.talir@nic.cz>
-----------------------------------------------

* release 1.9.0
* new Filter system, PageTable system refactored

2008-02-09 Jaromir Talir <jaromir.talir@nic.cz>
-----------------------------------------------

* release 1.8.0
* new function for getting registrar credit in _Admin.idl
* new type for table columns FILE_ID in _Admin.idl
* new function for inhibit letters generation in _Admin.idl
* autotools distribution
