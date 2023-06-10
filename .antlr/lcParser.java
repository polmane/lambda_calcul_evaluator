// Generated from c:\Users\polet\Documents\Mi Unidad\UPC\Info\LP\compilador\lambda_calcul\lc.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class lcParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, LLETRA=8, NOMMAC=9, 
		INFIX=10, WS=11;
	public static final int
		RULE_root = 0, RULE_terme = 1, RULE_conj = 2;
	private static String[] makeRuleNames() {
		return new String[] {
			"root", "terme", "conj"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'\u00E2\u2030\u00A1'", "'='", "'('", "')'", "'\u00CE\u00BB'", 
			"'\\'", "'.'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, "LLETRA", "NOMMAC", "INFIX", 
			"WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "lc.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public lcParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class RootContext extends ParserRuleContext {
		public RootContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_root; }
	 
		public RootContext() { }
		public void copyFrom(RootContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class RoottermContext extends RootContext {
		public TermeContext terme() {
			return getRuleContext(TermeContext.class,0);
		}
		public RoottermContext(RootContext ctx) { copyFrom(ctx); }
	}
	public static class DefmacContext extends RootContext {
		public TermeContext terme() {
			return getRuleContext(TermeContext.class,0);
		}
		public TerminalNode NOMMAC() { return getToken(lcParser.NOMMAC, 0); }
		public TerminalNode INFIX() { return getToken(lcParser.INFIX, 0); }
		public DefmacContext(RootContext ctx) { copyFrom(ctx); }
	}

	public final RootContext root() throws RecognitionException {
		RootContext _localctx = new RootContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_root);
		int _la;
		try {
			setState(10);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__2:
			case T__4:
			case T__5:
			case LLETRA:
				_localctx = new RoottermContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(6);
				terme(0);
				}
				break;
			case NOMMAC:
			case INFIX:
				_localctx = new DefmacContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(7);
				_la = _input.LA(1);
				if ( !(_la==NOMMAC || _la==INFIX) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(8);
				_la = _input.LA(1);
				if ( !(_la==T__0 || _la==T__1) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(9);
				terme(0);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TermeContext extends ParserRuleContext {
		public TermeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_terme; }
	 
		public TermeContext() { }
		public void copyFrom(TermeContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class AppContext extends TermeContext {
		public List<TermeContext> terme() {
			return getRuleContexts(TermeContext.class);
		}
		public TermeContext terme(int i) {
			return getRuleContext(TermeContext.class,i);
		}
		public AppContext(TermeContext ctx) { copyFrom(ctx); }
	}
	public static class AbsContext extends TermeContext {
		public ConjContext conj() {
			return getRuleContext(ConjContext.class,0);
		}
		public TermeContext terme() {
			return getRuleContext(TermeContext.class,0);
		}
		public AbsContext(TermeContext ctx) { copyFrom(ctx); }
	}
	public static class LetterContext extends TermeContext {
		public TerminalNode LLETRA() { return getToken(lcParser.LLETRA, 0); }
		public LetterContext(TermeContext ctx) { copyFrom(ctx); }
	}
	public static class TermContext extends TermeContext {
		public TermeContext terme() {
			return getRuleContext(TermeContext.class,0);
		}
		public TermContext(TermeContext ctx) { copyFrom(ctx); }
	}

	public final TermeContext terme() throws RecognitionException {
		return terme(0);
	}

	private TermeContext terme(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		TermeContext _localctx = new TermeContext(_ctx, _parentState);
		TermeContext _prevctx = _localctx;
		int _startState = 2;
		enterRecursionRule(_localctx, 2, RULE_terme, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(23);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__2:
				{
				_localctx = new TermContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(13);
				match(T__2);
				setState(14);
				terme(0);
				setState(15);
				match(T__3);
				}
				break;
			case T__4:
			case T__5:
				{
				_localctx = new AbsContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(17);
				_la = _input.LA(1);
				if ( !(_la==T__4 || _la==T__5) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(18);
				conj();
				setState(19);
				match(T__6);
				setState(20);
				terme(2);
				}
				break;
			case LLETRA:
				{
				_localctx = new LetterContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(22);
				match(LLETRA);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(29);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new AppContext(new TermeContext(_parentctx, _parentState));
					pushNewRecursionContext(_localctx, _startState, RULE_terme);
					setState(25);
					if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
					setState(26);
					terme(4);
					}
					} 
				}
				setState(31);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class ConjContext extends ParserRuleContext {
		public List<TerminalNode> LLETRA() { return getTokens(lcParser.LLETRA); }
		public TerminalNode LLETRA(int i) {
			return getToken(lcParser.LLETRA, i);
		}
		public ConjContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_conj; }
	}

	public final ConjContext conj() throws RecognitionException {
		ConjContext _localctx = new ConjContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_conj);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(33); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(32);
				match(LLETRA);
				}
				}
				setState(35); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==LLETRA );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 1:
			return terme_sempred((TermeContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean terme_sempred(TermeContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 3);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r(\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\3\2\3\2\3\2\3\2\5\2\r\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\5\3\32\n\3\3\3\3\3\7\3\36\n\3\f\3\16\3!\13\3\3\4\6\4$\n\4\r"+
		"\4\16\4%\3\4\2\3\4\5\2\4\6\2\5\3\2\13\f\3\2\3\4\3\2\7\b\2)\2\f\3\2\2\2"+
		"\4\31\3\2\2\2\6#\3\2\2\2\b\r\5\4\3\2\t\n\t\2\2\2\n\13\t\3\2\2\13\r\5\4"+
		"\3\2\f\b\3\2\2\2\f\t\3\2\2\2\r\3\3\2\2\2\16\17\b\3\1\2\17\20\7\5\2\2\20"+
		"\21\5\4\3\2\21\22\7\6\2\2\22\32\3\2\2\2\23\24\t\4\2\2\24\25\5\6\4\2\25"+
		"\26\7\t\2\2\26\27\5\4\3\4\27\32\3\2\2\2\30\32\7\n\2\2\31\16\3\2\2\2\31"+
		"\23\3\2\2\2\31\30\3\2\2\2\32\37\3\2\2\2\33\34\f\5\2\2\34\36\5\4\3\6\35"+
		"\33\3\2\2\2\36!\3\2\2\2\37\35\3\2\2\2\37 \3\2\2\2 \5\3\2\2\2!\37\3\2\2"+
		"\2\"$\7\n\2\2#\"\3\2\2\2$%\3\2\2\2%#\3\2\2\2%&\3\2\2\2&\7\3\2\2\2\6\f"+
		"\31\37%";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}