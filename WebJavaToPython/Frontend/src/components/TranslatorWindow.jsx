import propTypes from "prop-types";





const TranslatorWindow = ({ name, code, handler, color }) => {
  return (
    <div className={` bg-gradient-to-br ${color}  w-full p-4 pb-14 rounded-2xl`}>
      <label
        className="block text-gray-900 text-2xl font-bold mb-2 "
        htmlFor={`{name}Window`}
      >
        <p className="ml-3">{name}</p>
      </label>
      <textarea
        id={`{name}Window`}
        className="shadow appearance-none border rounded w-full h-full py-3 px-3 text-gray-400 bg-black bg-opacity-75 leading-tight overflow-auto resize-none"
        value={code}
        onChange={handler}
        spellCheck="false"
        
      ></textarea>
    </div>
  );
};

TranslatorWindow.propTypes = {
  name: propTypes.string.isRequired,
  code: propTypes.string.isRequired,
  handler: propTypes.func.isRequired,
  color: propTypes.string,
};

export default TranslatorWindow;
