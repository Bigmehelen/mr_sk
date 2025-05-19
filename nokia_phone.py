running = True 

while running:
	print("""
		Nokia 3310
		1. PhoneBook 
		2. Messages
		3. Chat
		4. Call register
		5. Tones
		6. Settings
		7. Call divert
		8. Games
		9. Calculator
		10. Reminders
		11. Clock
		12. Profiles
		13. Sim services
		  press 14 to Turn Off
		     """)
	
	users_phone_book = input("Choose an option: ")
	match users_phone_book:
		case "1":
			phone_book = True
			while phone_book:
				print("""
				Phone book
				1. search
				2. Services nos
				3. Add name
				4. Erase
				5. Edit
				6. Assign tone
				7. Send b'card
				8. Options
   				  1. Type of view
   				  2. Memory status
				9. Speed dials
				10. Voice tags

				press 0 to go back
				""")
				user_phone_book = input("Choose an option: ")
				match user_phone_book:
					case "1":
						print("""
						Search 
						""")
						search_box = true
						while search_box:
							print("""
					press 0 to go back
							""")
						phone = input("choose an option: ")
						match phone:
							case "0":
								search_box = false
							case _:
								print("Invalid input")
								continue

					case "2":
						print("""
						Service nos
					press 0 to go back
						""")
						service_nos = True
						while service_nos:
							users_service_nos = input("Choose an option: ")
							match users_service_nos:
								case "0": 
									service_nos = False
								case _:
									print("Invalid input")
									continue
					case "3":
						print("""
						Add names
					press 0 to go back
						""")
						add_names = True
						while add_names:
							users_add_names = input("Choose an option: ")
							match users_add_names:
								case "0": 
									add_names = False
								case _:
									print("Invalid input")
									continue

					case "4":
						print("""
						Erase
					press 0 to go back
						""")
						erase = True
						while erase:
							users_erase = input("Choose an option: ")
							match users_erase:
								case "0": 
									erase = False
								case _:
									print("Invalid input")
									continue

					case "5":
						print("""
						Edit
					press 0 to go back
						""")
						edit = True
						while edit:
							users_edit = input("Choose an option: ")
							match users_edit:
								case "0": 
									edit = False
								case _:
									print("Invalid input")
									continue

					case "6":
						print("""
						Assign Tones
					press 0 to go back
						""")
						assign_tones = True
						while assign_tones:
							users_assign_tones = input("Choose an option: ")
							match users_assign_tone:
								case "0": 
									assign_tones = False
								case _:
									print("Invalid input")
									continue

					case "7":
						print("""
						Send b'Card
					press 0 to go back
						""")
						send_card = True
						while send_card:
							users_send_card = input("Choose an option: ")
							match users_send_card:
								case "0": 
									send_card = False
								case _:
									print("Invalid input")
									continue

					case "8":
						print("""
						Options

						1. Type of view
   				  		2. Memory status

					press 00 to go back
						""")
						options = True
						while options:
							users_add_names = input("Choose an option: ")
							match users_add_names:
								case "1":
									print("""
									Type of view
								press 0 to go back
									""")
									type_view = True
									while type_view:
										users_type_view = input("Choose an option: ")
										match users_type_view:
											case "0": 
												type_view = False
											case _:
												print("Invalid input")
												continue
								case "2":
									print("""
									Memory status
								press 0 to go back
									""")
									memory_status = True
									while memory_status:
										users_memory_status = input("Choose an option: ")
										match users_memory_status:
											case "0": 
												memory_status = False
											case _:
												print("Invalid input")
												continue
								case "00": 
									options = False
								case _:
									print("Invalid input")
									continue

					case "9":
						print("""
						Speed dials
					press 0 to go back
						""")
						speed_dials = True
						while speed_dials:
							users_speed_dials = input("Choose an option: ")
							match users_speed_dials:
								case "0": 
									speed_dials = False
								case _:
									print("Invalid input")
									continue

					case "10":
						print("""
						Voice tags
					press 0 to go back
						""")
						voice_tags = True
						while voice_tags:
							users_voice_tags = input("Choose an option: ")
							match users_voice_tags:
								case "0": 
									voice_tags = False
								case _:
									print("Invalid input")
									continue
		
					case "0":
						phone_book = False
					case _: 
						print("Invalid Input")
						continue

		case "2":
			print("""
			Messages
			1. Write Messages
			2. Inbox
			3. Outbox
			4. Picture Messages
			5. Templates
			6. Smileys
			7. Message settings
 			   1. Set 1 
 				1. Message centre number
 				2. Message sent as 
 				3. Message validity			      	 
 			   2. Common
 				1. Delivery reports
 				2. Reply via same centre
 				3. Character support
			8. Info service
			9. Voice mailbox number
			10. Service command editor
			  press 11 to go back
			""")
			messages = True
			while messages:
				users_messages = input("Choose an option: ")
				match users_messages:
					case "1":
						print("""
					Write Messages
					press 0 to go back
						""")
						write_messages = True
						while write_messages:
							users_write_messages = input("Choose an option: ")
							match users_write_messages:
								case "0": 
									write_messages = False
								case _:
									print("Invalid input")
									continue

					case "2":
						print("""
						Inbox
					press 0 to go back
						""")
						inbox = True
						while inbox:
							users_inbox = input("Choose an option: ")
							match users_inbox:
								case "0": 
									inbox = False
								case _:
									print("Invalid input")
									continue

					case "3":
						print("""
						Outbox
					press 0 to go back
						""")
						outbox = True
						while outbox:
							users_outbox = input("Choose an option: ")
							match users_outbox:
								case "0": 
									outbox = False
								case _:
									print("Invalid input")
									continue

					case "4":
						print("""
						Picture Message
					press 0 to go back
						""")
						picture_message = True
						while picture_message:
							users_picture_message = input("Choose an option: ")
							match users_picture_message:
								case "0": 
									picture_message = False
								case _:
									print("Invalid input")
									continue

					case "5":
						print("""
						Templates
					press 0 to go back
						""")
						templates = True
						while templates:
							users_templates = input("Choose an option: ")
							match users_templates:
								case "0": 
									templates = False
								case _:
									print("Invalid input")
									continue

					case "6":
						print("""
						Smiley
					press 0 to go back
						""")
						smiley = True
						while smiley:
							users_smiley = input("Choose an option: ")
							match users_smiley:
								case "0": 
									smiley = False
								case _:
									print("Invalid input")
									continue
					case "7":
						print("""
						Message Setting
						1. Set 1 
 						   1. Message centre number
 						   2. Message sent as 
 						   3. Message validity
					press 4 to go back
						""")
						message_setting = True
						while message_setting:
							users_message_setting = input("Choose an option: ")
							match users_message_setting:
								case "1":
									print("""
									1. Set 1 
 						   			   1. Message centre number
									press 0 to go back
									""")
									set = True
									while set:
										users_set = input("Choose an option: ")
										match users_set:
											case "0": 
												set = False
											case _:
												print("Invalid input")
												continue

								case "2":
									print("""
									2. Message sent as 
									press 0 to go back
									""")
									message_sent = True
									while message_sent:
										users_message_sent = input("Choose an option: ")
										match users_message_sent:
											case "0": 
												message_sent = False
											case _:
												print("Invalid input")
												continue
								case "3":
									print("""
									3. Message validity
									press 0 to go back
									""")
									message_validity = True
									while message_validity:
										users_message_validity = input("Choose an option: ")
										match users_message_validity:
											case "0": 
												message_validity = False
											case _:
												print("Invalid input")
												continue

								case "4": 
									message_setting = False
								case _:
									print("Invalid input")
									continue
					case "8":
						print("""
						Info Service
					press 0 to go back
						""")
						info_service = True
						while info_service:
							users_info_service = input("Choose an option: ")
							match users_info_service:
								case "0": 
									info_service = False
								case _:
									print("Invalid input")
									continue

					case "9":
						print("""
						Voice mail box Number
					press 0 to go back
						""")
						voice_mail = True
						while voice_mail:
							users_voice_mail = input("Choose an option: ")
							match users_voice_mail:
								case "0": 
									voice_mail = False
								case _:
									print("Invalid input")
									continue

					case "10":
						print("""
						Service Command Editor
					press 0 to go back
						""")
						service_command = True
						while service_command:
							users_service_command = input("Choose an option: ")
							match users_service_command:
								case "0": 
									service_command = False
								case _:
									print("Invalid input")
									continue
					case "11": 
						messages = False
					case _:
						print("Invalid input")
						continue

		case "3":
			print("""
			Chat
			press 0 to go back
			""")
			chat = True
			while chat:
				users_chat = input("Choose an option: ")
				match users_chat:
					case "0": 
						chat = False
					case _:
						print("Invalid input")
						continue

		case "4":
			print("""
			Call Register
			1. Missed calls
			2. Recieved calls
			3. Dialled calls
			4. Erase recent calls
			5. Show call duration
			   1. Last call duration
			   2. All calls' duration
			   3. Recieved calls' duration
	 		   4. Dialled calls' duration
	 		   5. Clear timers
	 		6. Show call costs
			   1. Last call costs
	 		   2. All calls' cost
	  		   3. Clear counters
	 		7. Call cost settings
			   1. Call cost limit
			   2. Show costs in
			8. Prepaid credit
		
			Press 9 to go back
			""")
			call_register = True
			while call_register:
				users_call_register = input("Choose an option: ")
				match users_call_register:
					case "1":
						print("""
						Missed calls
					press 0 to go back
						""")
						missed_calls = True
						while missed_calls:
							users_missed_calls = input("Choose an option: ")
							match users_missed_calls:
								case "0": 
									missed_calls = False
								case _:
									print("Invalid input")
									continue

					case "2":
						print("""
						Recieved Calls
					press 0 to go back
						""")
						recieved_calls = True
						while recieved_calls:
							users_recieved_calls = input("Choose an option: ")
							match users_recieved_calls:
								case "0": 
									recieved_calls = False
								case _:
									print("Invalid input")
									continue

					case "3":
						print("""
						Dialled Calls
					press 0 to go back
						""")
						dialled_calls = True
						while dialled_calls:
							users_dialled_calls = input("Choose an option: ")
							match users_dialled_calls:
								case "0": 
									dialled_calls = False
								case _:
									print("Invalid input")
									continue

					case "4":
						print("""
						Erase Recent Calls
					press 0 to go back
						""")
						erase_calls = True
						while erase_calls:
							users_erase_calls = input("Choose an option: ")
							match users_erase_calls:
								case "0": 
									erase_calls = False
								case _:
									print("Invalid input")
									continue

					case "5":
						print("""
						Show Call Duration
					press 0 to go back
						""")
						show_calls = True
						while show_calls:
							users_show_calls = input("Choose an option: ")
							match users_show_calls:
								case "1":
									print("""
									Last Call Duration
								press 0 to go back
									""")
									last_calls = True
									while last_calls:
										users_last_calls = input("Choose an option: ")
										match users_last_calls:
											case "0": 
												last_calls = False
											case _:
												print("Invalid input")
												continue

								case "2":
									print("""
									All calls duration
								press 0 to go back
									""")
									all_calls = True
									while all_calls:
										users_all_calls = input("Choose an option: ")
										match users_all_calls:
											case "0": 
												all_calls = False
											case _:
												print("Invalid input")
												continue
								case "3":
									print("""
									Recieved calls duration
								press 0 to go back
									""")
									recieved_calls = True
									while all_calls:
										users_recieved_calls = input("Choose an option: ")
										match users_recieved_calls:
											case "0": 
												recieved_calls = False
											case _:
												print("Invalid input")
												continue
								case "4":
									print("""
									Dialled calls Duration 
								press 0 to go back
									""")
									dialled_calls = True
									while dialled_calls:
										users_dialled_calls = input("Choose an option: ")
										match users_dialled_calls:
											case "0": 
												dialled_calls = False
											case _:
												print("Invalid input")
												continue
								case "5":
									print("""
									Clear Timer
								press 0 to go back
									""")
									clear_timer = True
									while clear_timer:
										users_clear_timer = input("Choose an option: ")
										match users_clear_timer:
											case "0": 
												clear_timer = False
											case _:
												print("Invalid input")
												continue
					case "6":
						print("""
						Show Call Cost
					press 0 to go back
						""")
						show_cost = True
						while show_cost:
							users_show_cost = input("Choose an option: ")
							match users_show_cost:
								case "1":
									print("""
									Last Call Cost
									press 0 to go back
									""")
									last_cost = True
									while last_cost:
										users_last_cost = input("Choose an option: ")
										match users_last_cost:
											case "0": 
												last_cost = False
											case _:
												print("Invalid input")
												continue

								case "2":
									print("""
									All Call Cost
									press 0 to go back
									""")
									all_cost = True
									while all_cost:
										users_all_cost = input("Choose an option: ")
										match users_all_cost:
											case "0": 
												all_cost = False
											case _:
												print("Invalid input")
												continue
								case "3":
									print("""
									Clear Counter
									press 0 to go back
									""")
									counter = True
									while counter:
										users_counter = input("Choose an option: ")
										match users_counter:
											case "0": 
												counter = False
											case _:
												print("Invalid input")
												continue								
					case "7":
						print("""
						Show Call Setting
						press 0 to go back
						""")
						show_setting = True
						while show_setting:
							users_show_setting = input("Choose an option: ")
							match users_show_setting:
								case "1":
									print("""
									Call Cost Limit
								press 0 to go back
									""")
									cost_limit = True
									while cost_limit:
										users_cost_limit = input("Choose an option: ")
										match users_cost_limit:
											case "0": 
												cost_limit = False
											case _:
												print("Invalid input")
												continue
								case "2":
									print("""
									Show Cost in
								press 0 to go back
									""")
									cost_in = True
									while cost_in:
										users_cost_in = input("Choose an option: ")
										match users_cost_in:
											case "0": 
												cost_in = False
											case _:
												print("Invalid input")
												continue
								case "0": 
									show_setting = False
								case _:
									print("Invalid input")
									continue
					case "8":
						print("""
						Prepaid Credit
					press 0 to go back
						""")
						prepaid_credit = True
						while prepaid_credit:
							users_prepaid_credit = input("Choose an option: ")
							match users_prepaid_credit:
								case "0": 
									prepaid_credit = False
								case _:
									print("Invalid input")
									continue

					case "9": 
						call_register = False
					case _:
						print("Invalid input")
						continue

		case "5":
			print("""
			Tone
			1. Ringing Tone
			2. Ringing Volume
			3. Incoming call alerts
			4. Composer
			5. Message alert tone
			6. Keypad Tones
			7. Warning and games tones
			8. Vibrating alert
			9. Screen Saver
				press 10 to go back
			""")
			tone = True
			while tone:
				users_tone = input("Choose an option: ")
				match users_tone:
					case "1":
						print("""
						Ringing Tone
					press 0 to go back
						""")
						prepaid_credit = True
						while ringing_tone:
							users_ringing_tone = input("Choose an option: ")
							match users_ringing_tone:
								case "0": 
									ringing_tone = False
								case _:
									print("Invalid input")
									continue
					case "2":
						print("""
						Ringing Tone
					press 0 to go back
						""")
						ringing_tone = True
						while ringing_tone:
							users_ringing_tone  = input("Choose an option: ")
							match users_ringing_tone :
								case "0": 
									ringing_tone  = False
								case _:
									print("Invalid input")
									continue
					case "3":
						print("""
						Incoming Call
					press 0 to go back
						""")
						incoming_call = True
						while incoming_call:
							users_incoming_call = input("Choose an option: ")
							match users_incoming_call:
								case "0": 
									incoming_call = False
								case _:
									print("Invalid input")
									continue
					case "4":
						print("""
						Composer
					press 0 to go back
						""")
						composer = True
						while composer:
							users_composer = input("Choose an option: ")
							match users_composer:
								case "0": 
									composer = False
								case _:
									print("Invalid input")
									continue
					case "5":
						print("""
						Message Alert Tone
					press 0 to go back
						""")
						message_alert = True
						while message_alert:
							users_message_alert = input("Choose an option: ")
							match users_message_alert:
								case "0": 
									message_alert = False
								case _:
									print("Invalid input")
									continue
					case "6":
						print("""
						key Pad Tone
					press 0 to go back
						""")
						key_tone = True
						while key_tone:
							users_key_tone = input("Choose an option: ")
							match users_key_tone:
								case "0": 
									key_tone = False
								case _:
									print("Invalid input")
									continue
					case "7":
						print("""
						Warning and Game Tone
					press 0 to go back
						""")
						warning_tone = True
						while warning_tone:
							users_warning_tone = input("Choose an option: ")
							match users_warning_tone:
								case "0": 
									warning_tone = False
								case _:
									print("Invalid input")
									continue
					case "8":
						print("""
						Vibrating Alert
					press 0 to go back
						""")
						vibrating = True
						while vibrating:
							users_vibrating = input("Choose an option: ")
							match users_vibrating:
								case "0": 
									vibrating = False
								case _:
									print("Invalid input")
									continue
					case "9":
						print("""
						Screen Saver
					press 0 to go back
						""")
						screen_saver = True
						while screen_saver:
							users_screen_saver = input("Choose an option: ")
							match users_screen_saver:
								case "0": 
									screen_saver = False
								case _:
									print("Invalid input")
									continue
					case "10": 
						tone = False
					case _:
						print("Invalid input")
						continue
		case "6":
			print("""
			1.Settings
			   1. Automatic Redial
			   2. Speed dialing
			   3. Call Waiting options
			   4. Own number sending
			   5. Phone line in use
			   6. Automatic answer
			2. Phone Settings
			   1. Language
			   2. Cell info display
	  		   3. Welcome note
			   4. Network Selection
			   5. Lights
			   6. Confirm SIM service actions	
			3. Security settings
			   1. PIN code request
			   2. Call barring service
			   3. Fixed dialling
			   4. Closed user group
			   5. Phone security
			   6. Change access code
   			4. Restore to Factory default
				
			press 5 to go to back
			""")
			settings = True
			while settings:
				users_settings = input("Choose an option: ")
				match users_settings:
					case "1":
						print("""
						Settings
					press 5 to go back
						""")
						users_automatic_redial = input("Choose an option: ")
						match users_automatic_redial:
								case "1":
									print("""
									Automatic Redial
									press 0 to go back
										""")
									automatic_redial = True
									while automatic_redial:
										users_automatic_redial = input("Choose an option: ")
										match users_automatic_redial:
											case "0": 
												automatic_redial = False
											case _:
												print("Invalid input")
												continue
								case "2":
									print("""
									Speed dialling
									press 0 to go back
									""")
									speed_dialling = True
									while speed_dialling:
										users_speed_dialling = input("Choose an option: ")
										match users_speed_dialling:
											case "0": 
												speed_dialling = False
											case _:
												print("Invalid input")
												continue
								case "3":
									print("""
									Call Waiting Options
								press 0 to go back
									""")
									call_waiting = True
									while call_waiting:
										users_call_waiting = input("Choose an option: ")
										match users_call_waiting:
											case "0": 
												call_waiting = False
											case _:
												print("Invalid input")
												continue
								case "4":
									print("""
									Own Number Sending
								press 0 to go back
									""")
									own_number = True
									while own_number:
										users_own_number = input("Choose an option: ")
										match users_own_number:
											case "0": 
												own_number = False
											case _:
												print("Invalid input")
												continue
								case "5":
									print("""
									Phone Line in Use
								press 0 to go back
									""")
									phone_line = True
									while phone_line:
										users_phone_line = input("Choose an option: ")
										match users_phone_line:
											case "0": 
												phone_line = False
											case _:
												print("Invalid input")
												continue
								case "6":
									print("""
									Automatic Answer
								press 0 to go back
									""")
									automatic_answer = True
									while automatic_answer:
										users_automatic_answer = input("Choose an option: ")
										match users_automatic_answer:
											case "0": 
												automatic_answer = False
											case _:
												print("Invalid input")
												continue

					case "2":
						print("""
						Phone Settings
					press 0 to go back
						""")
						phone_settings = True
						while phone_settings:
							users_phone_settings = input("Choose an option: ")
							match users_phone_settings:
								case "1":
									print("""
									Language
									press 0 to go back
									""")
									language = True
									while language:
										users_language = input("Choose an option: ")
										match users_language:
											case "0": 
												language = False
											case _:
												print("Invalid input")
												continue
								case "2":
									print("""
									Cell Info Display
									press 0 to go back
									""")
									cell_info = True
									while cell_info:
										users_cell_info = input("Choose an option: ")
										match users_cell_info:
											case "0": 
												cell_info = False
											case _:
												print("Invalid input")
												continue

								case "3":
									print("""
									Welcome Note
									press 0 to go back
									""")
									welcome_notes = True
									while welcome_notes:
										users_welcome_notes = input("Choose an option: ")
										match users_welcome_notes:
											case "0": 
												welcome_notes = False
											case _:
												print("Invalid input")
												continue
								case "4":
									print("""
									Network Selection
									press 0 to go back
									""")
									network_selection = True
									while network_selection:
										users_network_selection = input("Choose an option: ")
										match users_network_selection:
											case "0": 
												network_selection = False
											case _:
												print("Invalid input")
												continue
								case "5":
									print("""
									Lights
									press 0 to go back
									""")
									lights = True
									while lights:
										users_lights = input("Choose an option: ")
										match users_lights:
											case "0": 
												lights = False
											case _:
												print("Invalid input")
												continue
								case "6":
									print("""
									Confirm Sim Service Actions
									press 0 to go back
									""")
									confirm_sim = True
									while confirm_sim:
										users_confirm_sim = input("Choose an option: ")
										match users_confirm_sim:
											case "0": 
												confirm_sim = False
											case _:
												print("Invalid input")
												continue
								case "0": 
									phone_settings = False
								case _:
									print("Invalid input")
									continue
					case "3":
						print("""
						Security Service
						press 0 to go back
						""")
						security_service = True
						while security_service:
							users_security_service = input("Choose an option: ")
							match users_security_service:
								case "1":
									print("""
									Pin Code Request
									press 0 to go back
									""")
									pin_code = True
									while pin_code:
										users_pin_code = input("Choose an option: ")
										match users_pin_code:
											case "0": 
												pin_code = False
											case _:
												print("Invalid input")
												continue
								case "2":
									print("""
									Call Barring Service
									press 0 to go back
									""")
									call_barring = True
									while call_barring:
										users_call_barring = input("Choose an option: ")
										match users_call_barring:
											case "0": 
												call_barring = False
											case _:
												print("Invalid input")
												continue
								case "3":
									print("""
									Fixed Dialling
									press 0 to go back
									""")
									fixed_dialling = True
									while fixed_dialling:
										users_fixed_dialling = input("Choose an option: ")
										match users_fixed_dialling:
											case "0": 
												fixed_dialling = False
											case _:
												print("Invalid input")
												continue
								case "4":
									print("""
									Closed user Group
									press 0 to go back
									""")
									closed_user = True
									while closed_user:
										users_closed_user = input("Choose an option: ")
										match users_closed_user:
											case "0": 
												closed_user = False
											case _:
												print("Invalid input")
												continue
								case "5":
									print("""
									Phone Security
									press 0 to go back
									""")
									phone_security = True
									while phone_security:
										users_phone_security = input("Choose an option: ")
										match users_phone_security:
											case "0": 
												phone_security = False
											case _:
												print("Invalid input")
												continue
								case "6":
									print("""
									Change Access Codes
									press 0 to go back
									""")
									change_access = True
									while change_access:
										users_change_access = input("Choose an option: ")
										match users_change_access:
											case "0": 
												change_access = False
											case _:
												print("Invalid input")
												continue
								case "0": 
									security_service = False
								case _:
									print("Invalid input")
									continue
					case "4":
						print("""
						Restore to factory Setting
						press 0 to go back
						""")
						restore_factory = True
						while restore_factory:
							users_restore_factory = input("Choose an option: ")
							match users_restore_factory:
								case "0": 
									restore_factory = False
								case _:
									print("Invalid input")
									continue
					case "5": 
						settings = False
					case _:
						print("Invalid input")
						continue
		case "7":
			print("""
			Call Divert
			press 0 to go back
			""")
			call_divert = True
			while call_divert:
				users_call_divert = input("Choose an option: ")
				match users_call_divert:
					case "0": 
						call_divert = False
					case _:
						print("Invalid input")
						continue
		case "8":
			print("""
			Games
			press 0 to go back
			""")
			games = True
			while games:
				users_games = input("Choose an option: ")
				match users_games:
					case "0": 
						games = False
					case _:
						print("Invalid input")
						continue
		case "9":
			print("""
			Calculator
			press 0 to go back
			""")
			calculator = True
			while calculator:
				users_calculator = input("Choose an option: ")
				match users_calculator:
					case "0": 
						calculator = False
					case _:
						print("Invalid input")
						continue
		case "10":
			print("""
			Reminder
			press 0 to go back
			""")
			reminder = True
			while reminder:
				users_reminder= input("Choose an option: ")
				match users_reminder:
					case "0": 
						reminder = False
					case _:
						print("Invalid input")
						continue
		case "11":
			print("""
			Clock
			1. Alarm
			2. Clock Setting
			3. Date setting
			4. Stopwatch
			5. Countdown
			6. Auto update of date and time
			press 7 to go back
			""")
			clock = True
			while clock:
				users_in_clock= input("Choose an option: ")
				match users_in_clock:
					case "1":
						print("""
						Alarm Clock
						press 0 to go back
						""")
						alarm_clock = True
						while alarm_clock:
							users_alarm_clock= input("Choose an option: ")
							match users_alarm_clock:
								case "0": 
									alarm_clock = False
								case _:
									print("Invalid input")
									continue
					case "2":
						print("""
						Clock Settings
						press 0 to go back
						""")
						clock_settings = True
						while clock_settings:
							users_clock_settings= input("Choose an option: ")
							match users_clock_settings:
								case "0": 
									clock_settings = False
								case _:
									print("Invalid input")
									continue
					case "3":
						print("""
						Date Settings
						press 0 to go back
						""")
						date_settings = True
						while date_settings:
							users_date_settings = input("Choose an option: ")
							match users_date_settings:
								case "0": 
									date_settings = False
								case _:
									print("Invalid input")
									continue
					case "4":
						print("""
						Stopwatch
						press 0 to go back
						""")
						stopwatch = True
						while stopwatch:
							users_stopwatch = input("Choose an option: ")
							match users_stopwatch:
								case "0": 
									stopwatch = False
								case _:
									print("Invalid input")
									continue
					case "5":
						print("""
						Countdown timer
						press 0 to go back
						""")
						countdown = True
						while countdown:
							users_countdown = input("Choose an option: ")
							match users_countdown:
								case "0": 
									countdown = False
								case _:
									print("Invalid input")
									continue
					case "6":
						print("""
						Auto update of Date and Time
						press 0 to go back
						""")
						auto_update = True
						while auto_update:
							users_auto_update = input("Choose an option: ")
							match users_auto_update:
								case "0": 
									auto_update = False
								case _:
									print("Invalid input")
									continue
					case "7": 
						clock = False
					case _:
						print("Invalid input")
						continue
		case "12":
			print("""
			Profiles
			press 0 to go back
			""")
			profiles = True
			while profiles:
				users_profiles = input("Choose an option: ")
				match users_profiles:
					case "0": 
						profiles = False
					case _:
						print("Invalid input")
						continue
		case "13":
			print("""
			Sim Services
			press 0 to go back
			""")
			sim_services = True
			while sim_services:
				users_sim_services = input("Choose an option: ")
				match users_sim_services:
					case "0": 
						sim_services = False
					case _:
						print("Invalid input")
						continue
		case "14":
			running = False
		case _: 
			print("Invalid Input")
			continue
