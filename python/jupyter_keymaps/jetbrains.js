/**
*
* Duplicate a current line in the Jupyter Notebook
* Used only CodeMirror API - https://codemirror.net
*
**/
CodeMirror.keyMap.pcDefault["Ctrl-D"] = function (cm) {

    // get a position of a current cursor in a current cell
    var current_cursor = cm.doc.getCursor();

    // read a content from a line where is the current cursor
    var line_content = cm.doc.getLine(current_cursor.line);

    // go to the end the current line
    CodeMirror.commands.goLineEnd(cm);

    // make a break for a new line
    CodeMirror.commands.newlineAndIndent(cm);

    // filled a content of the new line content from line above it
    cm.doc.replaceSelection(line_content);

    // restore position cursor on the new line
    cm.doc.setCursor(current_cursor.line + 1, current_cursor.ch);
};
/**
*
* Delete a current line in the Jupyter Notebook
* Used only CodeMirror API - https://codemirror.net
*
**/
CodeMirror.keyMap.pcDefault["Ctrl-Y"] = function (cm) {

    // delete line
    CodeMirror.commands.deleteLine(cm);
};