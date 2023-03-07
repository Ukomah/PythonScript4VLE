# Config
# 
InputFile= 'quiz.txt'
OutputFile = "export.xml"
correctmarker="> "


# Load list of questions from file

with open(InputFile, 'r') as file:
     lines = file.readlines()

# strips newlines
new_lst = [x[:-1] for x in lines]

# stores questions as a list inside a list
# like so:
# questionbank=[["q1", "q1t", "> ans11", "ans12", "ans13", "ans14"], ["q2", "q2t", "ans21", "> ans22", "ans23", "ans24"], ["q3", "q3t", "ans31", "ans32", "> ans33", "ans34"]]
questionbank = [new_lst[i:i+7] for i in range(0, len(new_lst), 7)]




ExportXML = open(OutputFile, "w")

# create a new file, with start of XML as provided by export function in moodle
L = """<?xml version="1.0" encoding="UTF-8"?>
<quiz>
<!-- question: 0  -->
  <question type="category">
    <category>
      <text>$course$/top/Default for ASpierredebrossestestpage</text>
    </category>
    <info format="moodle_auto_format">
      <text>The default category for questions shared in context 'ASpierredebrossestestpage'.</text>
    </info>
    <idnumber></idnumber>
  </question>

"""
ExportXML.write(L)
ExportXML.close

# switching file from overwrite to append mode
ExportXML = open(OutputFile, "a")


# parse questionbank into questions
for question in questionbank:
  # extracting atributes
  QuestionName=question[0]
  QuestionText=question[1]
  GeneralFeedback=""

  
  ChoiceText=[question[2], question[3], question[4], question[5]]
  ChoiceValue=[0,0,0,0]

  # establish correct answer, and assign 100 points for correct answer
  for i in range(0,len(ChoiceText)):
      if ChoiceText[i].__contains__(correctmarker):
        # strip correctmarker from correct answer
        ChoiceText[i]=ChoiceText[i][2:]
        ChoiceValue[i]=100



    

  # format string question according to moodle export.
  XML="""<!-- question: 13935748  -->
    <question type="multichoice">
      <name>
        <text>{QuestionName}</text>
      </name>
      <questiontext format="html">
        <text><![CDATA[<p dir="ltr" style="text-align: left;">{QuestionText}<br></p>]]></text>
      </questiontext>
      <generalfeedback format="html">
        <text><![CDATA[<p dir="ltr" style="text-align: left;">{GeneralFeedback}<br></p>]]></text>
      </generalfeedback>
      <defaultgrade>1.0000000</defaultgrade>
      <penalty>0.3333333</penalty>
      <hidden>0</hidden>
      <idnumber></idnumber>
      <single>true</single>
      <shuffleanswers>true</shuffleanswers>
      <answernumbering>abc</answernumbering>
      <showstandardinstruction>0</showstandardinstruction>
      <correctfeedback format="html">
        <text>Your answer is correct.</text>
      </correctfeedback>
      <partiallycorrectfeedback format="html">
        <text>Your answer is partially correct.</text>
      </partiallycorrectfeedback>
      <incorrectfeedback format="html">
        <text>Your answer is incorrect.</text>
      </incorrectfeedback>
      <shownumcorrect/>
      <answer fraction="{Choice1Value}" format="html">
        <text><![CDATA[<p dir="ltr" style="text-align: left;">{Choice1Text}<br></p>]]></text>
        <feedback format="html">
          <text><![CDATA[<p dir="ltr" style="text-align: left;">{Choice1Feedback}<br></p>]]></text>
        </feedback>
      </answer>
      <answer fraction="{Choice2Value}" format="html">
        <text><![CDATA[<p dir="ltr" style="text-align: left;">{Choice2Text}<br></p>]]></text>
        <feedback format="html">
          <text><![CDATA[<p dir="ltr" style="text-align: left;">{Choice2Feedback}<br></p>]]></text>
        </feedback>
      </answer>
      <answer fraction="{Choice3Value}" format="html">
        <text><![CDATA[<p dir="ltr" style="text-align: left;">{Choice3Text}<br></p>]]></text>
        <feedback format="html">
          <text><![CDATA[<p dir="ltr" style="text-align: left;">{Choice3Feedback}<br></p>]]></text>
        </feedback>
      </answer>
      <answer fraction="{Choice4Value}" format="html">
        <text><![CDATA[<p dir="ltr" style="text-align: left;">{Choice4Text}<br></p>]]></text>
        <feedback format="html">
          <text><![CDATA[<p dir="ltr" style="text-align: left;">{Choice4Feedback}<br></p>]]></text>
        </feedback>
      </answer>
    </question>

    """.format(
    QuestionName=  QuestionName, QuestionText = QuestionText,  GeneralFeedback=GeneralFeedback,  
    Choice1Value = ChoiceValue[0], Choice2Value = ChoiceValue[1], Choice3Value = ChoiceValue[2], Choice4Value = ChoiceValue[3], 
    Choice1Text = ChoiceText[0], Choice2Text = ChoiceText[1], Choice3Text = ChoiceText[2], Choice4Text = ChoiceText[3],
    Choice1Feedback = "", Choice2Feedback = "", Choice3Feedback = "", Choice4Feedback = ""
    )
  # append generated xml to output file
  ExportXML.write( XML)
  # print( QuestionName,  "\n", QuestionText, "\n",
  #   ChoiceValue[0], ChoiceValue[1], ChoiceValue[2], ChoiceValue[3], "\n",
  #   ChoiceText[0], "\n",ChoiceText[1], "\n",ChoiceText[2],  "\n",ChoiceText[3], "\n",)

# save file
ExportXML.write("</quiz>")
ExportXML.close