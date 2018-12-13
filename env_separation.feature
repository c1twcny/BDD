Feature: Environment Separation Policy

	Scenario Outline: Prod and Non-Prod Communication
		Given <env_1> assets can only communicate with other assets in the same type of environment 
		When <env_1> asset initiates a network L4 session with <env_2> asset on <condition> port(s) 
		Then network connection is <decision>

		Examples: Environment type and decision
		| env_1		| env_2		| condition	| decision	|
		| prod		| non-prod	| permitted	| denied	|
		| prod		| prod		| not-permitted	| denied	|
		| dev	 	| qa		| permitted	| granted	|
		| non-prod	| non-prod	| permitted	| granted	|
		| uat		| dev		| not-permitted	| denied	|
		| dr		| qa		| permitted	| denied	|
		| prod		| dr		| permitted	| granted	|

