from flask import Flask, Response, request, jsonify, redirect, flash, render_template
from config import *

def index():
    return ("<p> Hello World </p>")


def Parser():
    return render_template("Upload.html")