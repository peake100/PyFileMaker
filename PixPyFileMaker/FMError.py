# PyFileMaker - Integrating FileMaker and Python
# (c) 2014-2016 Marcin Kawa, kawa.macin@gmail.com
# (c) 2006-2008 Klokan Petr Pridal, klokan@klokan.cz
# (c) 2002-2006 Pieter Claerhout, pieter@yellowduck.be
# 
# http://code.google.com/p/pyfilemaker/
# http://www.yellowduck.be/filemaker/

# Import the main modules

FMErrorNum = {}
FMErrorNum[-1] = 'Unknown error'
FMErrorNum[0] = 'No error (success)'
FMErrorNum[1] = 'User canceled action'
FMErrorNum[2] = 'Memory error'
FMErrorNum[3] = 'Command is unavailable (for example, wrong operating system, wrong mode, etc.)'
FMErrorNum[4] = 'Command is unknown'
FMErrorNum[5] = 'Command is invalid (for example, a Set Field script step does not have a calculation specified)'
FMErrorNum[6] = 'File is read-only'
FMErrorNum[7] = 'Running out of memory'
FMErrorNum[8] = 'Empty result'
FMErrorNum[9] = 'Insufficient privileges'
FMErrorNum[10] = 'Requested data is missing'
FMErrorNum[11] = 'Name is not valid'
FMErrorNum[12] = 'Name already exists'
FMErrorNum[13] = 'File or object is in use'
FMErrorNum[14] = 'Out of range'
FMErrorNum[15] = 'Can\'t divide by zero'
FMErrorNum[16] = 'Operation failed, request retry (for example, a user query)'
FMErrorNum[17] = 'Attempt to convert foreign character set to UTF-16 failed'
FMErrorNum[18] = 'Client must provide account information to proceed'
FMErrorNum[19] = 'String contains characters other than A-Z, a-z, 0-9 (ASCII)'
FMErrorNum[20] = 'Command/operation cancelled by triggered script'
FMErrorNum[21] = 'Map Win 32 error of "ERROR_NOT_SUPPORTED". Microsoft documentation is "the request is not supported".'
FMErrorNum[26] = 'The file path specified is not a valid file path'
FMErrorNum[100] = 'File is missing'
FMErrorNum[101] = 'Record is missing'
FMErrorNum[102] = 'Field is missing'
FMErrorNum[103] = 'Relationship is missing'
FMErrorNum[104] = 'Script is missing'
FMErrorNum[105] = 'Layout is missing'
FMErrorNum[106] = 'Table is missing'
FMErrorNum[107] = 'Index is missing'
FMErrorNum[108] = 'Value list is missing'
FMErrorNum[109] = 'Privilege set is missing'
FMErrorNum[110] = 'Related tables are missing'
FMErrorNum[111] = 'Field repetition is invalid'
FMErrorNum[112] = 'Window is missing'
FMErrorNum[113] = 'Function is missing'
FMErrorNum[114] = 'File reference is missing'
FMErrorNum[115] = 'Specified menu set is not present'
FMErrorNum[116] = 'Specified layout object is not present'
FMErrorNum[117] = 'Specified data source is not present'
FMErrorNum[130] = 'Files are damaged or missing and must be reinstalled'
FMErrorNum[131] = 'Language pack files are missing (such as template files)'
FMErrorNum[200] = 'Record access is denied'
FMErrorNum[201] = 'Field cannot be modified'
FMErrorNum[202] = 'Field access is denied'
FMErrorNum[203] = 'No records in file to print, or password doesn\'t allow print access'
FMErrorNum[204] = 'No access to field(s) in sort order'
FMErrorNum[205] = 'User does not have access privileges to create new records; import will overwrite existing data'
FMErrorNum[206] = 'User does not have password change privileges, or file is not modifiable'
FMErrorNum[207] = 'User does not have sufficient privileges to change database schema, or file is not modifiable'
FMErrorNum[208] = 'Password does not contain enough characters'
FMErrorNum[209] = 'New password must be different from existing one'
FMErrorNum[210] = 'User account is inactive'
FMErrorNum[211] = 'Password has expired'
FMErrorNum[212] = 'Invalid user account and/or password. Please try again'
FMErrorNum[213] = 'User account and/or password does not exist'
FMErrorNum[214] = 'Too many login attempts'
FMErrorNum[215] = 'Administrator privileges cannot be duplicated'
FMErrorNum[216] = 'Guest account cannot be duplicated'
FMErrorNum[217] = 'User does not have sufficient privileges to modify administrator accountUser does not have sufficient privileges to modify administrator account'
FMErrorNum[218] = 'Password and verify password do not match (iPhone)'
FMErrorNum[300] = 'File is locked or in use'
FMErrorNum[301] = 'Record is in use by another user'
FMErrorNum[302] = 'Table is in use by another user'
FMErrorNum[303] = 'Database schema is in use by another user'
FMErrorNum[304] = 'Layout is in use by another user'
FMErrorNum[306] = 'Record modification ID does not match'
FMErrorNum[307] = 'Lost connection to the host and the transaction could not relock'
FMErrorNum[400] = 'Find criteria are empty'
FMErrorNum[401] = 'No records match the request'
FMErrorNum[402] = 'Selected field is not a match field for a lookup'
FMErrorNum[403] = 'Exceeding maximum record limit for trial version of FileMaker Pro'
FMErrorNum[404] = 'Sort order is invalid'
FMErrorNum[405] = 'Number of records specified exceeds number of records that can be omitted'
FMErrorNum[406] = 'Replace/Reserialize criteria are invalid'
FMErrorNum[407] = 'One or both match fields are missing (invalid relationship)'
FMErrorNum[408] = 'Specified field has inappropriate data type for this operation'
FMErrorNum[409] = 'Import order is invalid'
FMErrorNum[410] = 'Export order is invalid'
FMErrorNum[412] = 'Wrong version of FileMaker Pro used to recover file'
FMErrorNum[413] = 'Specified field has inappropriate field type'
FMErrorNum[414] = 'Layout cannot display the result'
FMErrorNum[415] = 'One or more required related records are not available'
FMErrorNum[416] = 'Primary key required from data source table'
FMErrorNum[417] = 'Database is not supported for ODBC operations'
FMErrorNum[418] = 'The base directory specified in the CREATE TABLE ... field blob EXTERNAL \'path\' not found'
FMErrorNum[500] = 'Date value does not meet validation entry options'
FMErrorNum[501] = 'Time value does not meet validation entry options'
FMErrorNum[502] = 'Number value does not meet validation entry options'
FMErrorNum[503] = 'Value in field is not within the range specified in validation entry options'
FMErrorNum[504] = 'Value in field is not unique as required in validation entry options'
FMErrorNum[505] = 'Value in field is not an existing value in the database file as required in validation entry options'
FMErrorNum[506] = 'Value in field is not listed on the value list specified in validation entry option'
FMErrorNum[507] = 'Value in field failed calculation test of validation entry option'
FMErrorNum[508] = 'Invalid value entered in Find mode'
FMErrorNum[509] = 'Field requires a valid value'
FMErrorNum[510] = 'Related value is empty or unavailable'
FMErrorNum[511] = 'Value in field exceeds maximum field size'
FMErrorNum[512] = 'Record was already modified by another user'
FMErrorNum[513] = 'Record must have a value in some field to be created'
FMErrorNum[600] = 'Print error has occurred'
FMErrorNum[601] = 'Combined header and footer exceed one page'
FMErrorNum[602] = 'Body doesn\'t fit on a page for current column setup'
FMErrorNum[603] = 'Print connection lost'
FMErrorNum[700] = 'File is of the wrong file type for import'
FMErrorNum[706] = 'EPSF file has no preview image'
FMErrorNum[707] = 'Graphic translator cannot be found'
FMErrorNum[708] = 'Can\'t import the file or need color monitor support to import file'
FMErrorNum[709] = 'QuickTime movie import failed'
FMErrorNum[710] = 'Unable to update QuickTime reference because the database file is read-only'
FMErrorNum[711] = 'Import translator cannot be found'
FMErrorNum[714] = 'Password privileges do not allow the operation'
FMErrorNum[715] = 'Specified Excel worksheet or named range is missing'
FMErrorNum[716] = 'A SQL query using DELETE, INSERT, or UPDATE is not allowed for ODBC import'
FMErrorNum[717] = 'There is not enough XML/XSL information to proceed with the import or export'
FMErrorNum[718] = 'Error in parsing XML file (from Xerces)'
FMErrorNum[719] = 'Error in transforming XML using XSL (from Xalan)'
FMErrorNum[720] = 'Error when exporting; intended format does not support repeating fields'
FMErrorNum[721] = 'Unknown error occurred in the parser or the transformer'
FMErrorNum[722] = 'Cannot import data into a file that has no fields'
FMErrorNum[723] = 'You do not have permission to add records to or modify records in the target table'
FMErrorNum[724] = 'You do not have permission to add records to the target table'
FMErrorNum[725] = 'You do not have permission to modify records in the target table'
FMErrorNum[726] = 'There are more records in the import file than in the target table. Not all records were imported'
FMErrorNum[727] = 'There are more records in the target table than in the import file. Not all records were updated'
FMErrorNum[729] = 'Errors occurred during import. Records could not be imported'
FMErrorNum[730] = 'Unsupported Excel version. (Convert file to Excel 7.0 (Excel 95), Excel 97, 2000, or XP format and try again)'
FMErrorNum[731] = 'The file you are importing from contains no data'
FMErrorNum[732] = 'This file cannot be inserted because it contains other files'
FMErrorNum[733] = 'A table cannot be imported into itself'
FMErrorNum[734] = 'This file type cannot be displayed as a picture'
FMErrorNum[735] = 'This file type cannot be displayed as a picture. It will be inserted and displayed as a file'
FMErrorNum[736] = 'Too much data to export to this format. It will be truncated'
FMErrorNum[737] = 'Bento table is reported as missed when trying to import it'
FMErrorNum[800] = 'Unable to create file on disk'
FMErrorNum[801] = 'Unable to create temporary file on System disk'
FMErrorNum[802] = 'Unable to open file'
FMErrorNum[803] = 'File is single user or host cannot be found'
FMErrorNum[804] = 'File cannot be opened as read-only in its current state'
FMErrorNum[805] = 'File is damaged; use Recover command'
FMErrorNum[806] = 'File cannot be opened with this version of FileMaker Pro'
FMErrorNum[807] = 'File is not a FileMaker Pro file or is severely damaged'
FMErrorNum[808] = 'Cannot open file because access privileges are damaged'
FMErrorNum[809] = 'Disk/volume is full'
FMErrorNum[810] = 'Disk/volume is locked'
FMErrorNum[811] = 'Temporary file cannot be opened as FileMaker Pro file'
FMErrorNum[813] = 'Record Synchronization error on network'
FMErrorNum[814] = 'File(s) cannot be opened because maximum number is open'
FMErrorNum[815] = 'Couldn\'t open lookup file'
FMErrorNum[816] = 'Unable to convert file'
FMErrorNum[817] = 'Unable to open file because it does not belong to this solution'
FMErrorNum[819] = 'Cannot save a local copy of a remote file'
FMErrorNum[820] = 'File is in the process of being closed'
FMErrorNum[821] = 'Host forced a disconnect'
FMErrorNum[822] = 'FMI files not found; reinstall missing files'
FMErrorNum[823] = 'Cannot set file to single-user, guests are connected'
FMErrorNum[824] = 'File is damaged or not a FileMaker file'
FMErrorNum[825] = 'File is not authorized to reference the protected file'
FMErrorNum[850] = 'This path is not valid (for the platform it represents)'
FMErrorNum[851] = 'The external file can not be deleted from disk. Do you want to delete the reference to the file anyway?'
FMErrorNum[852] = 'Can not write file to the external storage.'
FMErrorNum[853] = 'One or more containers failed to transfer'
FMErrorNum[900] = 'General spelling engine error'
FMErrorNum[901] = 'Main spelling dictionary not installed'
FMErrorNum[902] = 'Could not launch the Help system'
FMErrorNum[903] = 'Command cannot be used in a shared file'
FMErrorNum[905] = 'No active field selected; command can only be used if there is an active field'
FMErrorNum[906] = 'Current file must be shared in order to use this command'
FMErrorNum[920] = 'Can\'t initialize the spelling engine'
FMErrorNum[921] = 'User dictionary cannot be loaded for editing'
FMErrorNum[922] = 'User dictionary cannot be found'
FMErrorNum[923] = 'User dictionary is read-only'
FMErrorNum[951] = 'An unexpected error occurred'
FMErrorNum[954] = 'Unsupported XML grammar'
FMErrorNum[955] = 'No database name'
FMErrorNum[956] = 'Maximum number of database sessions exceeded'
FMErrorNum[957] = 'Conflicting commands'
FMErrorNum[958] = 'Parameter missing'
FMErrorNum[1200] = 'Generic calculation error'
FMErrorNum[1201] = 'Too few parameters in the function'
FMErrorNum[1202] = 'Too many parameters in the function'
FMErrorNum[1203] = 'Unexpected end of calculation'
FMErrorNum[1204] = 'Number, text constant, field name or "(" expected'
FMErrorNum[1205] = 'Comment is not terminated with "*/"'
FMErrorNum[1206] = 'Text constant must end with a quotation mark'
FMErrorNum[1207] = 'Unbalanced parenthesis'
FMErrorNum[1208] = 'Operator missing, function not found or "(" not expected'
FMErrorNum[1209] = 'Name (such as field name or layout name) is missing'
FMErrorNum[1210] = 'Plug-in function has already been registered'
FMErrorNum[1211] = 'List usage is not allowed in this function'
FMErrorNum[1212] = 'An operator (for example, +, -, *) is expected here'
FMErrorNum[1213] = 'This variable has already been defined in the Let function'
FMErrorNum[1214] = 'AVERAGE, COUNT, EXTEND, GETREPETITION, MAX, MIN, NPV, STDEV, SUM and GETSUMMARY: expression found where a field alone is needed'
FMErrorNum[1215] = 'This parameter is an invalid Get function parameter'
FMErrorNum[1216] = 'Only Summary fields allowed as first argument in GETSUMMARY'
FMErrorNum[1217] = 'Break field is invalid'
FMErrorNum[1218] = 'Cannot evaluate the number'
FMErrorNum[1219] = 'A field cannot be used in its own formula'
FMErrorNum[1220] = 'Field type must be normal or calculated'
FMErrorNum[1221] = 'Data type must be number, date, time, or timestamp'
FMErrorNum[1222] = 'Calculation cannot be stored'
FMErrorNum[1223] = 'The function is not implemented'
FMErrorNum[1224] = 'The function is not defined'
FMErrorNum[1225] = 'The function is not supported in this context'
FMErrorNum[1300] = 'The specified name can\'t be used'
FMErrorNum[1400] = 'ODBC driver initialization failed; make sure the ODBC drivers are properly installed'
FMErrorNum[1401] = 'Failed to allocate environment (ODBC)'
FMErrorNum[1402] = 'Failed to free environment (ODBC)'
FMErrorNum[1403] = 'Failed to disconnect (ODBC)'
FMErrorNum[1404] = 'Failed to allocate connection (ODBC)'
FMErrorNum[1405] = 'Failed to free connection (ODBC)'
FMErrorNum[1406] = 'Failed check for SQL API (ODBC)'
FMErrorNum[1407] = 'Failed to allocate statement (ODBC)'
FMErrorNum[1408] = 'Extended error (ODBC)'
FMErrorNum[1409] = 'Error (ODBC)'
FMErrorNum[1413] = 'Failed communication link (ODBC)'
FMErrorNum[1414] = 'ODBC/SQL Statement Too Long'
FMErrorNum[1450] = 'Action requires PHP privilege extension'
FMErrorNum[1451] = 'Action requires that current file be remote'
FMErrorNum[1501] = 'The authentication Failed.'
FMErrorNum[1502] = 'The connection was refused by the SMTP server.'
FMErrorNum[1503] = 'There was an error with SSL.'
FMErrorNum[1504] = 'The server required the connection to be encrypted.'
FMErrorNum[1505] = 'The specified authentication is not supported by the SMTP server.'
FMErrorNum[1506] = 'Email(s) could not be sent successfully.'
FMErrorNum[1507] = 'Unable to login into the SMTP Server.'
FMErrorNum[1550] = 'The file isn\'t a plugin, or can\'t load for some reason'
FMErrorNum[1551] = 'Can\'t delete existing plugin, can\'t write to the folder, can\'t put on disk for some reason'
FMErrorNum[1626] = 'The protocol is not supported'
FMErrorNum[1627] = 'The authentication Failed.'
FMErrorNum[1628] = 'There was an error with SSL.'
FMErrorNum[1629] = 'The connection timed out'
FMErrorNum[1630] = 'The url format is incorrect'
FMErrorNum[1631] = 'The connection failed'
FMErrorNum[2021] = 'plug-ins configuration disallowed'
FMErrorNum[2046] = 'This command or action cannot be performed because that functionality is no longer supported'
FMErrorNum[2047] = 'Bento 2 (or later) is not presented on the system'
FMErrorNum[2048] = 'The selected work book is not excel 2007/2008 format'
FMErrorNum[2056] = 'This script step cannot be performed because this window is in a modal state.'
FMErrorNum[3000] = 'Action never occurred because script was triggered'
FMErrorNum[3001] = 'Set when a step returns but is not really finished (probably due to having to switch threads and keep engine thread running)'
FMErrorNum[3002] = 'The external file can not be deleted from disk. Do you want to delete the reference to the file anyway?'
FMErrorNum[3003] = 'Can not write file to the external storage.'
FMErrorNum[3004] = 'Directory Cant Edit'
FMErrorNum[3005] = 'Directory Cant Delete'
FMErrorNum[3100] = 'Theme is in use'
FMErrorNum[3219] = 'Convert Global To Remote Warning'
FMErrorNum[3220] = 'Directory Not Accessible Warning'
FMErrorNum[3316] = 'Wrning before clearing out existing find requests'
FMErrorNum[3317] = 'Wrning before attempting to restore files from hibernation'
FMErrorNum[3427] = 'Button cannot contain a tab control [NEW in FMP 8.0, modified in FMP 13.0'
FMErrorNum[3428] = 'When a panel is deleted, all the objects on that panel will be deleted [NEW in FMP 8.0, modified in FMP 13.0'
FMErrorNum[3429] = 'One or more of the panels you\'ve selected contain locked objects. Do you you want to delete those panel(s) even though they contain locked object(s)? [NEW in FMP 8.0, modified in FMP 13.0]'
FMErrorNum[3956] = 'The total size of all base directory paths cannot exceed ^1 bytes.'
FMErrorNum[3958] = 'Please select at least one bar code type'
FMErrorNum[3957] = 'At least one filter must remain.'
FMErrorNum[4103] = 'File path is invalid or cannot be resolved during file transfer'
FMErrorNum[4104] = 'File i/o issue during file transfer'
FMErrorNum[4106] = 'The target base directory is not valid.'
FMErrorNum[4107] = 'The target base directory could not be created.'
FMErrorNum[4603] = 'Spell Export Complete'
FMErrorNum[7100] = 'Data Deferred'
FMErrorNum[8404] = 'An installed OnTimer script could not be found or could not be run with current access privileges'
FMErrorNum[8213] = 'Too many temporary objects created, can\'t create any more.'
FMErrorNum[8310] = 'There is an error in the syntax of the query.'
FMErrorNum[8498] = 'Stale Import Order To Be Updated'
FMErrorNum[8499] = 'Import Match May Be Invalid'
FMErrorNum[20413] = 'Too Many Files'
FMErrorNum[20605] = 'No network connection is available'
FMErrorNum[20606] = 'Fail to resolve network address'

class FMError( Exception ):
    """Exception related to operation with FM."""

class FMFieldError( Exception ):
    """Exception for missing field inside of FM (e.g. FMError 102)."""

class FMServerError( FMError ):
    """Exception caused by FileMaker Server"""

def FMErrorByNum( num ):
    """This function raises an error based on the specified error code."""

    if not num in FMErrorNum.keys():
        raise FMServerError(num, FMErrorNum[-1])
    elif num == 102:
        raise FMFieldError(num, FMErrorNum[num])
    else:
        raise FMServerError(num, FMErrorNum[num])
